import abc
import importlib

from typing import Iterable

from .transforms import Transform


class InteroperableTarget:
    KNOWN_TARGET_TYPES = {'ieee_1547_1': 'IEEE_1547_1',
                          'iec_61850_7_420': 'IEC_61850_7_420',
                          'ieee_1815_2': 'IEEE_1815_2',
                          'ieee_2030_5': 'IEEE_2030_5',
                          'sun_spec_modbus': 'SunSpecModbus'}
    MAPPING = {}  # r'(\[.*'[^']+), (.*)],' --> r'$1', '$2],'
    CUSTOM_TRANSFORMS = {}

    def __init__(self, **kwargs):
        Transform.add_transforms(self.CUSTOM_TRANSFORMS)
        self.target_mapping = {k: None for targets in self.MAPPING.values() for k in targets}
        self.ieee1547_mapping = {
            ieee1547_name: Transform.factory(target_mapping=self.target_mapping, **v)
            for ieee1547_name, v in self.MAPPING.items()
        }

    def get(self, point_names: Iterable[str]) -> dict[str, any] | bool:
        poll_request = set()
        ret_dict = {}
        for point in point_names:
            poll_request.add(self.ieee1547_mapping[point].mapped_points)
        if self.poll_values(poll_request):
            for point in point_names:
                ret_dict.update(self.ieee1547_mapping[point].read())
            return ret_dict
        else:
            return False

    def set(self, point_value_dict: dict[str, any]):
        request_dict = {}
        for point, value in point_value_dict.items():
            if self.ieee1547_mapping[point].writable():
                request_dict.update(self.ieee1547_mapping[point].prep_write(value))
        return self.set_values(request_dict)

    def constant_pf_mode(self, enable, inject_absorption_setting, excitation_setting):
        success = False
        request_dict = {}
        request_dict.update(self.ieee1547_mapping[f'constant_pf_mode_inject_absorption_setting'].prep_write(
            inject_absorption_setting))
        request_dict.update(self.ieee1547_mapping[f'constant_pf_mode_excitation_setting'].prep_write(excitation_setting))
        if self.set_values(request_dict):
            success = self.ieee1547_mapping[f'constant_pf_mode_enable'].prep_write(enable)
        return success

    def volt_var_mode(self, enable, v_ref, autonomous_v_ref_adjustment_enable, v_ref_adjustment_time_constant,
                      v_q_curve_points, open_loop_response_time):
        success = False
        request_dict = {}
        request_dict.update(self.ieee1547_mapping[f'volt_var_mode_v_ref'].prep_write(v_ref))
        request_dict.update(self.ieee1547_mapping[f'volt_var_mode_autonomous_v_ref_adjustment_enable'].prep_write(
            autonomous_v_ref_adjustment_enable))
        request_dict.update(self.ieee1547_mapping[f'volt_var_mode_v_ref_adjustment_time_constant'].prep_write(
            v_ref_adjustment_time_constant))
        request_dict.update(self.ieee1547_mapping[f'volt_var_mode_v_q_curve_points'].prep_write( v_q_curve_points))
        request_dict.update(self.ieee1547_mapping[f'volt_var_mode_open_loop_response_time'].prep_write(
            open_loop_response_time))
        if self.set_values(request_dict):
            success = self.ieee1547_mapping[f'volt_var_mode_enable'].prep_write(enable)
        return success

    def watt_var_mode(self, enable, p_q_curve_points):
        success = False
        request_dict = {}
        request_dict.update(self.ieee1547_mapping[f'watt_var_mode_p_q_curve_points'].prep_write(p_q_curve_points))
        if self.set_values(request_dict):
            success = self.ieee1547_mapping[f'watt_var_mode_enable'].prep_write(enable)
        return success

    def constant_var_mode(self, enable, var_setting):
        success = False
        request_dict = {}
        request_dict.update(self.ieee1547_mapping[f'constant_var_modevar_setting'].prep_write(var_setting))
        if self.set_values(request_dict):
            success = self.ieee1547_mapping[f'constant_var_mode_enable'].prep_write(enable)
        return success

    def volt_watt_mode(self, enable, v_p_curve_points, open_loop_response_time):
        success = False
        request_dict = {}
        request_dict.update(self.ieee1547_mapping[f'volt_wattv_p_curve_points'].prep_write(v_p_curve_points))
        request_dict.update(self.ieee1547_mapping[f'volt_wattopen_loop_response_time'].prep_write(
            open_loop_response_time))
        if self.set_values(request_dict):
            success = self.ieee1547_mapping[f'volt_watt_mode_enable'].prep_write(enable)
        return success

    def voltage_trip_mode(self, hv_trip_curve_points, lv_trip_curve_points):
        # TODO: Does this really have an enable which is missing from the table?
        request_dict = {}
        request_dict.update(self.ieee1547_mapping[f'volttage_trip_mode_hv_trip_curve_points'].prep_write(
            hv_trip_curve_points))
        request_dict.update(self.ieee1547_mapping[f'volttage_trip_mode_lv_trip_curve_points'].prep_write(
            lv_trip_curve_points))
        return self.set_values(request_dict)

    def momentary_cessation_mode(self, hv_trip_curve_points, lv_trip_curve_points):
        # TODO: Does this really have an enable which is missing from the table?
        request_dict = {}
        request_dict.update(self.ieee1547_mapping[f'momentary_cessation_mode_hv_trip_curve_points'].prep_write(
            hv_trip_curve_points))
        request_dict.update(self.ieee1547_mapping[f'momentary_cessation_mode_lv_trip_curve_points'].prep_write(
            lv_trip_curve_points))
        return self.set_values(request_dict)

    def frequency_trip_mode(self, hv_trip_curve_points, lv_trip_curve_points):
        # TODO: Does this really have an enable which is missing from the table?
        request_dict = {}
        request_dict.update(self.ieee1547_mapping[f'frequency_trip_mode_hv_trip_curve_points'].prep_write(
            hv_trip_curve_points))
        request_dict.update(self.ieee1547_mapping[f'frequency_trip_mode_lv_trip_curve_points'].prep_write(
            lv_trip_curve_points))
        return self.set_values(request_dict)

    def frequency_watt_mode(self, dbof, dbuf, kof, kuf, open_loop_response_time):
        success = False
        request_dict = {}
        request_dict.update(self.ieee1547_mapping[f'frequency_watt_mode_dbof'].prep_write(dbof))
        request_dict.update(self.ieee1547_mapping[f'frequency_watt_mode_dbuf'].prep_write(dbuf))
        request_dict.update(self.ieee1547_mapping[f'frequency_watt_mode_kof'].prep_write(kof))
        request_dict.update(self.ieee1547_mapping[f'frequency_watt_mode_kuf'].prep_write(kuf))
        request_dict.update(self.ieee1547_mapping[f'frequency_watt_mode_open_loop_response_time'].prep_write(
            open_loop_response_time))
        if self.set_values(request_dict):
            success = self.ieee1547_mapping[f'frequency_watt_enable'].prep_write(enable)
        return success

    def enter_service(self, permit_service, es_voltage_high, es_voltage_low, es_frequency_high,
                      es_frequency_low, es_delay, es_randomized_delay, es_ramp_time):
        success = False
        request_dict = {}
        request_dict.update(self.ieee1547_mapping[f'enter_service_es_voltage_high'].prep_write(es_voltage_high))
        request_dict.update(self.ieee1547_mapping[f'enter_service_es_voltage_low'].prep_write(es_voltage_low))
        request_dict.update(self.ieee1547_mapping[f'enter_service_es_frequency_high'].prep_write(es_frequency_high))
        request_dict.update(self.ieee1547_mapping[f'enter_service_es_frequency_low'].prep_write(es_frequency_low))
        request_dict.update(self.ieee1547_mapping[f'enter_service_es_delay'].prep_write(es_delay))
        request_dict.update(self.ieee1547_mapping[f'enter_service_es_randomized_delay'].prep_write(es_randomized_delay))
        request_dict.update(self.ieee1547_mapping[f'enter_service_es_ramp_time'].prep_write(es_ramp_time))
        if self.set_values(request_dict):
            success = self.set_values(self.ieee1547_mapping[f'enter_service_permit_service'].prep_write(permit_service))
        return success
    
    def limit_watt_mode(self, enable, watt_setting):
        success = False
        if self.set_values(self.ieee1547_mapping[f'limit_watt_mode_watt_setting'].prep_write(watt_setting)):
            success = self.ieee1547_mapping[f'limit_watt_mode_enable'].prep_write(enable)
        return success

    @abc.abstractmethod
    def poll_values(self, point_names: Iterable) -> bool:
        """Request a set of points from the target. Update the self.target_mapping dictionary."""
        pass
    
    @abc.abstractmethod
    def set_values(self, request_dict: dict[str, any]) -> bool:
        """Set points from the target. Return success bool."""
        pass
    
    @classmethod
    def factory(cls, config):
        target_type = config.pop('target_type', None)
        target_module = config.pop('target_module', f'interoperability.{target_type}')
        target_class_name = config.pop('target_class')
        if not target_class_name and target_type in cls.KNOWN_TARGET_TYPES:
            target_class_name = cls.KNOWN_TARGET_TYPES[target_type]
        if target_module == 'interoperability.' or not target_class_name:
            raise KeyError('Target configuration does not specify either a known target type or valid module and class.')
        module = importlib.import_module(target_module)
        target_class = getattr(module, target_class_name)
        if not issubclass(target_class, cls):
            raise TypeError('Invalid target class: '
                            '{target_module}.{target_class_name} is not a subclass of InteroperableTarget.')
        return target_class(**config)
