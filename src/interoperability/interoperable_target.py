import abc
import importlib
import logging

from typing import Dict, Iterable, Union

from importlib.metadata import version
if int(version('volttron').split('.')[0]) >= 10:
    from volttron.utils import setup_logging
else:
    # noinspection PyUnresolvedReferences
    from volttron.platform.agent.utils import setup_logging


from .transforms import Transform

setup_logging()
_log = logging.getLogger(__name__)


class InteroperableTarget:
    KNOWN_TARGET_TYPES = {'ieee_1547_1': 'IEEE_1547_1',
                          'iec_61850_7_420': 'IEC_61850_7_420',
                          'ieee_1815_2': 'IEEE_1815_2',
                          'ieee_2030_5': 'IEEE_2030_5',
                          'sunspec_modbus': 'SunSpecModbus'}
    MAPPING = {}  # r'(\[.*'[^']+), (.*)],' --> r'$1', '$2],'
    CUSTOM_TRANSFORMS = {}

    def __init__(self, parent, **kwargs):
        if kwargs:
            _log.warning(f'InteroperableTarget base class received extra parameters {list(kwargs.keys())}')
        Transform.add_transforms(self.CUSTOM_TRANSFORMS)
        self.parent = parent
        self.target_mapping = {k: None for targets in self.MAPPING.values() for k in targets}
        self.ieee61850_mapping = {
            ieee61850_name: Transform.factory(target_mapping=self.target_mapping, ieee61850_name=ieee61850_name, **v)
            for ieee61850_name, v in self.MAPPING.items()
        }

    def get(self, point_names: Iterable[str]) -> Union[Dict[str, any], bool]:
        get_request = {}
        ret_dict = {}
        _log.debug(f'point names is: {point_names}')
        for point in point_names:
            for p in self.ieee61850_mapping[point].mapped_points:
                _log.debug(f'point is: {point},  p is: {p}')
                get_request[p] = point
        _log.debug('get_request:')
        _log.debug(get_request)
        if self.get_values(get_request):
            for point in point_names:
                ret_dict.update(self.ieee61850_mapping[point].read())
            return ret_dict
        else:
            return False

    def set(self, point_value_dict: Dict[str, any]):
        request_dict = {}
        for point, value in point_value_dict.items():
            if self.ieee61850_mapping[point].writable():
                request_dict.update(self.ieee61850_mapping[point].prep_write(value))
        return self.set_values(request_dict)

    def constant_pf_mode(self, enable, inject_setting, absorption_setting, excitation_setting):
        success = False
        request_dict = {}
        request_dict.update(self.ieee61850_mapping['DFPF.PFGnTgt'].prep_write(
            inject_setting))
        request_dict.update(self.ieee61850_mapping['DFPF.PFLodTgt'].prep_write(
            absorption_setting))
        request_dict.update(self.ieee61850_mapping['DFPF.PFExtSet'].prep_write(excitation_setting))
        if self.set_values(request_dict):
            success = self.ieee61850_mapping['DFPF.ModEna'].prep_write(enable)
        return success

    def volt_var_mode(self, enable, v_ref, autonomous_v_ref_adjustment_enable, v_ref_adjustment_time_constant,
                      v_q_curve_points, open_loop_response_time):
        success = False
        request_dict = {}
        request_dict.update(self.ieee61850_mapping['DECP.VRef'].prep_write(v_ref))
        request_dict.update(self.ieee61850_mapping['DVVR.VRefAdjEna'].prep_write(
            autonomous_v_ref_adjustment_enable))
        request_dict.update(self.ieee61850_mapping['DVVR.VRefTmms'].prep_write(
            v_ref_adjustment_time_constant))
        request_dict.update(self.ieee61850_mapping['DVVR.VVArCrv'].prep_write( v_q_curve_points))
        request_dict.update(self.ieee61850_mapping['DVVR.OpnLoopMax'].prep_write(
            open_loop_response_time))
        if self.set_values(request_dict):
            success = self.ieee61850_mapping['DVVR.ModEna'].prep_write(enable)
        return success

    def watt_var_mode(self, enable, p_q_curve_points):
        success = False
        request_dict = {}
        request_dict.update(self.ieee61850_mapping['DWVR.WVArCrv'].prep_write(p_q_curve_points))
        if self.set_values(request_dict):
            success = self.ieee61850_mapping['DWVR.ModEna'].prep_write(enable)
        return success

    def constant_var_mode(self, enable, var_setting):
        success = False
        request_dict = {}
        request_dict.update(self.ieee61850_mapping['DVAR.VArTgt'].prep_write(var_setting))
        if self.set_values(request_dict):
            success = self.ieee61850_mapping['DVAR.ModEna'].prep_write(enable)
        return success

    def volt_watt_mode(self, enable, v_p_curve_points, open_loop_response_time):
        success = False
        request_dict = {}
        request_dict.update(self.ieee61850_mapping['DVWC.VWCrv'].prep_write(v_p_curve_points))
        request_dict.update(self.ieee61850_mapping['DVWC.OpnLoopMax'].prep_write(
            open_loop_response_time))
        if self.set_values(request_dict):
            success = self.ieee61850_mapping['DVWC.ModEna'].prep_write(enable)
        return success

    def voltage_trip_mode(self, hv_trip_curve_points, lv_trip_curve_points):
        # TODO: These are not just two points.  How do these really come in?
        # TODO: IEC names do not seem to be unique, nor do they match the 1547_mappings sheet.
        # TODO: Does this really have an enable which is missing from the table?
        request_dict = {}
        request_dict.update(self.ieee61850_mapping[f'volttage_trip_mode_hv_trip_curve_points'].prep_write(
            hv_trip_curve_points))
        request_dict.update(self.ieee61850_mapping[f'volttage_trip_mode_lv_trip_curve_points'].prep_write(
            lv_trip_curve_points))
        return self.set_values(request_dict)

    def momentary_cessation_mode(self, hv_trip_curve_points, lv_trip_curve_points):
        # TODO: These are not just two points.  How do these really come in?
        # TODO: IEC names do not seem to be unique, nor do they match the 1547_mappings sheet.
        # TODO: Does this really have an enable which is missing from the table?
        request_dict = {}
        request_dict.update(self.ieee61850_mapping[f'momentary_cessation_mode_hv_trip_curve_points'].prep_write(
            hv_trip_curve_points))
        request_dict.update(self.ieee61850_mapping[f'momentary_cessation_mode_lv_trip_curve_points'].prep_write(
            lv_trip_curve_points))
        return self.set_values(request_dict)

    def frequency_trip_mode(self, hv_trip_curve_points, lv_trip_curve_points):
        # TODO: Does this really have an enable which is missing from the table?
        # TODO: These are not just two points.  How do these really come in?
        # TODO: IEC names do not seem to be unique, nor do they match the 1547_mappings sheet.
        request_dict = {}
        request_dict.update(self.ieee61850_mapping[f'frequency_trip_mode_hv_trip_curve_points'].prep_write(
            hv_trip_curve_points))
        request_dict.update(self.ieee61850_mapping[f'frequency_trip_mode_lv_trip_curve_points'].prep_write(
            lv_trip_curve_points))
        return self.set_values(request_dict)

    def frequency_watt_mode(self, enable, dbof, dbuf, kof, kuf, open_loop_response_time):
        success = False
        request_dict = {}
        request_dict.update(self.ieee61850_mapping['DHFW.HzStr'].prep_write(dbof))
        request_dict.update(self.ieee61850_mapping['DLFW.HzStr'].prep_write(dbuf))
        request_dict.update(self.ieee61850_mapping['DHFW.WGra'].prep_write(kof))
        request_dict.update(self.ieee61850_mapping['DLFW.WGra'].prep_write(kuf))
        # TODO: There has to be a better way than to make the key two keys with a comma.... (These collapse to one point in concrete protocols).
        request_dict.update(self.ieee61850_mapping['DHFW.OpnLoopMax, DLFW.OpnLoopMax'].prep_write(open_loop_response_time))
        if self.set_values(request_dict):
            # TODO: Enable point was missing from 1547mappsings sheet. It is 711.Ena in SunspecModbus.
            #  According to MESA_DER_PICS spreadsheet, it is "DHFW.Mod" in 61850, but that all shall enables as "*.Mod",
            #  where the 1547_mappings sheet has "*.ModEna" for most other functions.
            success = self.ieee61850_mapping[f'DHFW.Mod'].prep_write(enable)
        return success

    def enter_service(self, permit_service, es_voltage_high, es_voltage_low, es_frequency_high,es_frequency_low, es_delay, es_randomized_delay, es_ramp_time):
        success = False
        request_dict = {}
        request_dict.update(self.ieee61850_mapping[f'DCTE.VHiLim'].prep_write(es_voltage_high))
        request_dict.update(self.ieee61850_mapping[f'DCTE.VLoLim'].prep_write(es_voltage_low))
        request_dict.update(self.ieee61850_mapping[f'DCTE.HzHiLim'].prep_write(es_frequency_high))
        request_dict.update(self.ieee61850_mapping[f'DCTE.HzLoLim'].prep_write(es_frequency_low))
        request_dict.update(self.ieee61850_mapping[f'DCTE.RtnSrvDlyTim'].prep_write(es_delay))
        request_dict.update(self.ieee61850_mapping[f'DCTE.RtnSrvDlyTim'].prep_write(es_randomized_delay))
        request_dict.update(self.ieee61850_mapping[f'DCTE.RtnSrvRmpTim'].prep_write(es_ramp_time))
        if self.set_values(request_dict):
            # TODO: How to handle this double point? DCTE.RtnSrvAuto, DCTE.RtnSrvAuth
            success = self.set_values(self.ieee61850_mapping[f'enter_service_permit_service'].prep_write(permit_service))
        return success
    
    def limit_watt_mode(self, enable, watt_setting):
        success = False
        if self.set_values(self.ieee61850_mapping[f'limit_watt_mode_watt_setting'].prep_write(watt_setting)):
            success = self.ieee61850_mapping[f'limit_watt_mode_enable'].prep_write(enable)
        return success

    @abc.abstractmethod
    def get_values(self, point_names: Iterable) -> bool:
        """Request a set of points from the target. Update the self.target_mapping dictionary."""
        pass
    
    @abc.abstractmethod
    def set_values(self, request_dict: Dict[str, any]) -> bool:
        """Set points from the target. Return success bool."""
        pass
    
    @classmethod
    def factory(cls, parent, config):
        target_type = config.pop('target_type', None)
        target_module = config.pop('target_module', f'interoperability.target_classes.{target_type}')
        target_class_name = config.pop('target_class', None)
        if not target_class_name and target_type in cls.KNOWN_TARGET_TYPES:
            target_class_name = cls.KNOWN_TARGET_TYPES[target_type]
        if target_module == 'interoperability.target_classes.' or not target_class_name:
            raise KeyError('Target configuration does not specify either a known target type or valid module and class.')
        module = importlib.import_module(target_module)
        target_class = getattr(module, target_class_name)
        if not issubclass(target_class, cls):
            raise TypeError('Invalid target class: '
                            '{target_module}.{target_class_name} is not a subclass of InteroperableTarget.')
        return target_class(parent=parent, **config)
