import logging

from typing import Dict

from importlib.metadata import version
if int(version('volttron').split('.')[0]) >= 10:
    from volttron.utils import setup_logging
else:
    # noinspection PyUnresolvedReferences
    from volttron.platform.agent.utils import setup_logging


from interoperability.interoperable_target import InteroperableTarget

setup_logging()
_log = logging.getLogger(__name__)


class SunSpecModbus(InteroperableTarget):
    def __init__(self, driver_device_topic, **kwargs):
        super(SunSpecModbus, self).__init__(**kwargs)
        self.topic = driver_device_topic

    def get_values(self, point_names: Dict[str, str]) -> bool:
        # Takes input of dict[sunspec_name, iec_name].
        _log.debug(f'#### In get_values (sunspec_modbus), point_names is:')
        _log.debug(point_names)
        responses, errors = self.parent.vip.rpc.call('platform.driver', 'get_multiple_points', self.topic,
                                                     list(point_names.keys())).get()
        if errors:
            _log.warning(f'Failed to read to some points: {errors}')
            return False
        for k, v in responses.items():
            point_name = k.split('/')[-1]
            self.target_mapping[point_names[point_name]] = v
        return True

    def set_values(self, request_dict: Dict[str, any]) -> bool:
        _log.debug(f'#### In set_values (sunspec_modbus), request_dict is:')
        _log.debug(request_dict)
        error_dict = self.parent.vip.rpc.call('platform.driver', 'set_multiple_points', self.topic,
                                              list(request_dict.items())).get()
        if error_dict:
            _log.warning(f'Failed to write to some points: {error_dict}')
            return False
        return True

    MAPPING = {'DGEN.WMaxRtg': {'mapped_points': '702.WMaxRtg',
                                'transform_type': 'one_to_one',
                                'writable': False},
               'DGEN.WGnOvPFRtg': {'mapped_points': '702.WOvrExtRtg',
                                   'transform_type': 'one_to_one',
                                   'writable': True},
               'DGEN.OvPFRtg': {'mapped_points': '702.WOvrExtRtgPF',
                                'transform_type': 'one_to_one',
                                'writable': True},
               'DGEN.WGnUnPFRtg': {'mapped_points': '702.WUndExtRtg',
                                   'transform_type': 'one_to_one',
                                   'writable': False},
               'DGEN.UnPFRtg': {'mapped_points': '702.WUndExtRtgPF',
                                'transform_type': 'one_to_one',
                                'writable': False},
               'DGEN.VAMaxRtg': {'mapped_points': '702.VAMaxRtg',
                                 'transform_type': 'one_to_one',
                                 'writable': False},
               'DGEN.Ieee1547Cat1': {'mapped_points': '702.NorOpCatRtg',
                                     'transform_type': 'one_to_one',
                                     'writable': True},
               'DGEN.Ieee1547Cat2': {'mapped_points': '702.AbnOpCatRtg',
                                     'transform_type': 'one_to_one',
                                     'writable': True},
               'DGEN.VarMaxSupRtg': {'mapped_points': '702.VarMaxInjRtg',
                                     'transform_type': 'one_to_one',
                                     'writable': False},
               'DGEN.VarMaxAbgRtg': {'mapped_points': '702.VarMaxIAbsRtg',
                                     'transform_type': 'one_to_one',
                                     'writable': False},
               'DSTO.WChaUnPFRtg': {'mapped_points': '702.WChaRteMaxRtg',
                                    'transform_type': 'one_to_one',
                                    'writable': False},
               'DSTO.VAMaxChaRtg': {'mapped_points': '702.WChaRteMaxRtg',
                                    'transform_type': 'one_to_one',
                                    'writable': False},
               'DECP.VRef': {'mapped_points': '702.VNomRtg',
                             'transform_type': 'one_to_one',
                             'writable': False},
               'DGEN.VMaxRtg': {'mapped_points': '702.VMaxRtg',
                                'transform_type': 'one_to_one',
                                'writable': False},
               'DGEN.VMinRtg': {'mapped_points': '702.VMinRtg',
                                'transform_type': 'one_to_one',
                                'writable': False},
               'DVRT, DFRT, DFWP, DWLM, DVWC, DFWC, DVAR, DFPF, DVVC, DWVR': {'mapped_points': '702.CtrlModes',
                                                                              'transform_type': 'unknown',
                                                                              'writable': False},
               'DGEN.SuscRtg': {'mapped_points': '702.ReactSusceptRtg',
                                'transform_type': 'one_to_one',
                                'writable': False},
               'LPHD.PhyNam.vendor': {'mapped_points': '1.Mn',
                                      'transform_type': 'one_to_one',
                                      'writable': False},
               'LPHD.PhyNam.model': {'mapped_points': '1.Md',
                                     'transform_type': 'one_to_one',
                                     'writable': False},
               'LPHD.PhyNam.serNum': {'mapped_points': '1.SN',
                                      'transform_type': 'one_to_one',
                                      'writable': False},
               'LPHD.PhyNam.swRev': {'mapped_points': '1.Vr',
                                     'transform_type': 'one_to_one',
                                     'writable': False},
               # TODO: Why is this nan?
               # 'DSTO.WhRtg': {'mapped_points': nan,
               #                'transform_type': 'one_to_one',
               #                'writable': False},
               'DGEN.WMax': {'mapped_points': '702.WMaxRtg',
                             'transform_type': 'one_to_one',
                             'writable': False},
               'DGEN.VAMax': {'mapped_points': '702.VAMaxRtg',
                              'transform_type': 'one_to_one',
                              'writable': False},
               'DGEN.RegCap': {'mapped_points': '702.IntIslandCat',
                               'transform_type': 'one_to_one',
                               'writable': False},
               # TODO: Why is this nan?
               # 'DGEN.Vmax': {'mapped_points': nan,
               #               'transform_type': 'one_to_one',
               #               'writable': False},
               # TODO: Why is this nan?
               # 'DGEN.Vmin': {'mapped_points': nan,
               #               'transform_type': 'one_to_one',
               #               'writable': False},
               'DECP.MMXU.TotW': {'mapped_points': '701.W',
                                  'transform_type': 'one_to_one',
                                  'writable': False},
               'DECP.MMXU.TotVAr': {'mapped_points': '701.Var',
                                    'transform_type': 'one_to_one',
                                    'writable': False},
               'DECP.MMXU.PhV.phsA.mag, DECP.MMXU.PhV.phsB.mag, DECP.MMXU.PhV.phsC.mag': {
                   'mapped_points': '701.LLV, 701.LNV, 701.VL1L2, 701.VL1, 701.VL2L3, 701.VL2, 701.VL3L1, 701.VL3',
                   'transform_type': 'map_list',
                   'writable': False},
               'DECP.MMXU.Hz': {'mapped_points': '701.Hz',
                                'transform_type': 'one_to_one',
                                'writable': False},
               'DGEN.DERState': {'mapped_points': '701.St',
                                 'transform_type': 'one_to_one',
                                 'writable': False},
               'DSTO.DERState.1': {'mapped_points': '701.ConnSt',
                                   'transform_type': 'one_to_one',
                                   'writable': False},
               'CALH.GrAlm': {'mapped_points': '701.Alrm',
                              'transform_type': 'one_to_one',
                              'writable': False},
               'DSTO.SocUsePct': {'mapped_points': '713.SoC',
                                  'transform_type': 'one_to_one',
                                  'writable': False},
               'DFPF.ModEna': {'mapped_points': '704.PFWInjEna',
                               'transform_type': 'one_to_one',
                               'writable': False},
               'DFPF.PFGnTgt, DFPF.PFLodTgt': {'mapped_points': '704.PFWInj.PF',
                                               'transform_type': 'unknown',
                                               'writable': False},
               'DFPF.PFExtSet': {'mapped_points': '704.PFWInj.Ext',
                                 'transform_type': 'one_to_one',
                                 'writable': False},
               'DVVR.ModEna': {'mapped_points': '705.Ena',
                               'transform_type': 'one_to_one',
                               'writable': False},
               'DVVR.VRefAdjEna': {'mapped_points': '705.VRefAutoEna',
                                   'transform_type': 'one_to_one',
                                   'writable': False},
               'DVVR.VRefTmms': {'mapped_points': '705.VRefAutoTms',
                                 'transform_type': 'one_to_one',
                                 'writable': False},
               'DVVR.VVArCrv': {'mapped_points': '705.Crv.Pt[#].V, 705.Crv.Pt[#].Var',
                                'transform_type': 'broadcast',
                                'writable': False},
               'DVVR.OpnLoopMax': {'mapped_points': '705.RspTms',
                                   'transform_type': 'one_to_one',
                                   'writable': False},
               'DWVR.ModEna': {'mapped_points': '712.Ena',
                               'transform_type': 'one_to_one',
                               'writable': False},
               'DWVR.WVArCrv': {'mapped_points': '712.Crv.Pt[#].W, 712.Crv.Pt[#].Var',
                                'transform_type': 'broadcast',
                                'writable': False},
               'DVAR.ModEna': {'mapped_points': '704.VarSetEna',
                               'transform_type': 'one_to_one',
                               'writable': False},
               'DVAR.VArTgt': {'mapped_points': '704.VarSetPct',
                               'transform_type': 'one_to_one',
                               'writable': False},
               'DVWC.ModEna': {'mapped_points': '706.Ena',
                               'transform_type': 'one_to_one',
                               'writable': False},
               'DVWC.VWCrv': {'mapped_points': '706.Crv.Pt[#].V, 706.Crv.Pt[#].W',
                              'transform_type': 'broadcast',
                              'writable': False},
               'DVWC.OpnLoopMax': {'mapped_points': '706.RspTms',
                                   'transform_type': 'one_to_one',
                                   'writable': False},
               'DHVT.TrZnSt, PTOV.TmVCrv': {'mapped_points': '707.MustTrip.Crv.Pt[#].V, 707.MustTrip.Crv.Pt[#].Tms',
                                            'transform_type': 'map_list',
                                            'writable': False},
               'DLVT.TrZnSt, PTUV.TmVCrv': {'mapped_points': '708.MustTrip.Crv.Pt[#].V, 708.MustTrip.Crv.Pt[#].Tms',
                                            'transform_type': 'map_list',
                                            'writable': False},
               'DHVT.CeaZnSt, PTOV.TmVCrv': {'mapped_points': '707.MomCess.Crv.Pt[#].V, 707.MomCess.Crv.Pt[#].Tms',
                                             'transform_type': 'map_list',
                                             'writable': False},
               'DLVT.CeaZnSt, PTUV.TmVCrv': {'mapped_points': '708.MomCess.Crv.Pt[#].V, 708.MomCess.Crv.Pt[#].Tms',
                                             'transform_type': 'map_list',
                                             'writable': False},
               'DHFT.TrZnSt, PTOF.StrVal': {'mapped_points': '709.MustTrip.Crv.Pt[#].Hz, 707.MustTrip.Crv.Pt[#].Tms',
                                            'transform_type': 'map_list',
                                            'writable': False},
               'DLFT.TrZnSt, PTUF.StrVal': {'mapped_points': '710.MustTrip.Crv.Pt[#].Hz, 710.MustTrip.Crv.Pt[#].Tms',
                                            'transform_type': 'map_list',
                                            'writable': False},
               'DHFW.HzStr': {'mapped_points': '711.Ctl.DbOf',
                              'transform_type': 'one_to_one',
                              'writable': True},
               'DLFW.HzStr': {'mapped_points': '711.Ctl.DbUf',
                              'transform_type': 'one_to_one',
                              'writable': False},
               'DHFW.WGra': {'mapped_points': '711.Ctl.KOf',
                             'transform_type': 'one_to_one',
                             'writable': True},
               'DLFW.WGra': {'mapped_points': '711.Ctl.Kuf',
                             'transform_type': 'one_to_one',
                             'writable': False},
               'DHFW.OpnLoopMax, DLFW.OpnLoopMax': {'mapped_points': '711.Ctl.RspTms',
                                                    'transform_type': 'unknown',
                                                    'writable': False},
               'DCTE.RtnSrvAuto, DCTE.RtnSrvAuth': {'mapped_points': '703.ES',
                                                    'transform_type': 'unknown',
                                                    'writable': False},
               'DCTE.VHiLim': {'mapped_points': '703.ESVHi',
                               'transform_type': 'one_to_one',
                               'writable': False},
               'DCTE.VLoLim': {'mapped_points': '703.ESVLo',
                               'transform_type': 'one_to_one',
                               'writable': False},
               'DCTE.HzHiLim': {'mapped_points': '703.ESHzHi',
                                'transform_type': 'one_to_one',
                                'writable': False},
               'DCTE.HzLoLim': {'mapped_points': '703.ESHzLo',
                                'transform_type': 'one_to_one',
                                'writable': False},
               'DCTE.RtnSrvDlyTim': {'mapped_points': '703.ESDlyTms',
                                     'transform_type': 'one_to_one',
                                     'writable': False},
               'DCTE.RtnSrvRmpTim': {'mapped_points': '703.ESRmpTms',
                                     'transform_type': 'one_to_one',
                                     'writable': False},
               'DWMX.ModEna, DWMN.ModEna': {'mapped_points': '704.WMaxLimPctEna',
                                            'transform_type': 'unknown',
                                            'writable': False},
               'DWMX.LimW, DWMN.LimW': {'mapped_points': '704.WMaxLimPct',
                                        'transform_type': 'unknown',
                                        'writable': False}}

    #     {
    #     'Nameplate	Active Power (unity)': {
    #         'mapped_points': ['702.WMaxRtg'],
    #         'transform_type': 'one_to_one',
    #         'writable': False
    #     },
    #     'Nameplate	Active Power (over-excited)': {
    #         'mapped_points': ['702.WOvrExtRtg'],
    #         'transform_type': 'one_to_one',
    #         'writable': False
    #     },
    #     'Nameplate	Power Factor (over-excited)': {
    #         'mapped_points': ['702.WOvrExtRtgPF'],
    #         'transform_type': 'one_to_one',
    #         'writable': False
    #     },
    #     'Nameplate	Active Power (under-excited)': {
    #         'mapped_points': ['702.WUndExtRtg'],
    #         'transform_type': 'one_to_one',
    #         'writable': False
    #     },
    #     'Nameplate	Power Factor (under-excited)': {
    #         'mapped_points': ['702.WUndExtRtgPF'],
    #         'transform_type': 'one_to_one',
    #         'writable': False
    #     },
    #     'Nameplate	Apparent Power (Max)': {
    #         'mapped_points': ['702.VAMaxRtg'],
    #         'transform_type': 'one_to_one',
    #         'writable': False
    #     },
    #     'Nameplate	Normal (operating category)': {
    #         'mapped_points': ['702.NorOpCatRtg'],
    #         'transform_type': 'one_to_one',
    #         'writable': False
    #     },
    #     'Nameplate	Abnormal (operating category)': {
    #         'mapped_points': ['702.AbnOpCatRtg'],
    #         'transform_type': 'one_to_one',
    #         'writable': False
    #     },
    #     'Nameplate	Reactive Power (Max Injected)': {
    #         'mapped_points': ['702.VarMaxInjRtg'],
    #         'transform_type': 'one_to_one',
    #         'writable': False
    #     },
    #     'Nameplate	Reactive Power (Max Absorbed)': {
    #         'mapped_points': ['702.VarMaxIAbsRtg'],
    #         'transform_type': 'one_to_one',
    #         'writable': False
    #     },
    #     'Nameplate	Active Power (Max Charge)': {
    #         'mapped_points': ['702.WChaRteMaxRtg'],
    #         'transform_type': 'one_to_one',
    #         'writable': False
    #     },
    #     'Nameplate	Apparent Power (Max Charge)': {
    #         'mapped_points': ['702.WChaRteMaxRtg'],
    #         'transform_type': 'one_to_one',
    #         'writable': False
    #     },
    #     'Nameplate	Voltage AC (nominal)': {
    #         'mapped_points': ['702.VNomRtg'],
    #         'transform_type': 'one_to_one',
    #         'writable': False
    #     },
    #     'Nameplate	Voltage AC (max)': {
    #         'mapped_points': ['702.VMaxRtg'],
    #         'transform_type': 'one_to_one',
    #         'writable': False
    #     },
    #     'Nameplate	Voltage AC (min)': {
    #         'mapped_points': ['702.VMinRtg'],
    #         'transform_type': 'one_to_one',
    #         'writable': False
    #     },
    #     'Nameplate	Supported Control Mode Functions': {
    #         'mapped_points': ['702.CtrlModes'],
    #         'transform_type': 'one_to_one',
    #         'writable': False
    #     },
    #     'Nameplate	Reactive Susceptance': {
    #         'mapped_points': ['702.ReactSusceptRtg'],
    #         'transform_type': 'one_to_one',
    #         'writable': False
    #     },
    #     'Nameplate	Manufacturer': {
    #         'mapped_points': ['1.Mn'],
    #         'transform_type': 'one_to_one',
    #         'writable': False
    #     },
    #     'Nameplate	Model': {
    #         'mapped_points': ['1.Md'],
    #         'transform_type': 'one_to_one',
    #         'writable': False
    #     },
    #     'Nameplate	Serial Number': {
    #         'mapped_points': ['1.SN'],
    #         'transform_type': 'one_to_one',
    #         'writable': False
    #     },
    #     'Nameplate	Version': {
    #         'mapped_points': ['1.Vr'],
    #         'transform_type': 'one_to_one',
    #         'writable': False
    #     },
    #     'Nameplate	Storage Capacity': {
    #         'mapped_points': [],
    #         'transform_type': 'exclude',
    #         'writable': False
    #     },
    #     'Configuration	Active Power (unity)': {
    #         'mapped_points': ['702.Wmax'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Configuration	Active Power (over-excited)': {
    #         'mapped_points': ['702.WMaxOvrExt'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Configuration	Power Factor (over-excited)': {
    #         'mapped_points': ['702.WOvrExtPF'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Configuration	Active Power (under-excited)': {
    #         'mapped_points': ['702.WMaxUndExt'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Configuration	Power Factor (under-excited)': {
    #         'mapped_points': ['702.WUndExtPF'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Configuration	Apparent Power (Max)': {
    #         'mapped_points': ['702.VAMax'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Configuration	Normal (operating category)': {
    #         'mapped_points': ['702.IntIslandCat'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Configuration	Abnormal (operating category)': {
    #         'mapped_points': [],
    #         'transform_type': 'exclude',
    #         'writable': False
    #     },
    #     'Configuration	Reactive Power (Max Injected)': {
    #         'mapped_points': ['702.VarMaxInjRtg'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Configuration	Reactive Power (Max Absorbed)': {
    #         'mapped_points': ['702.VarMaxAbsRtg'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Configuration	Active Power (Max Charge)': {
    #         'mapped_points': ['702.WChaRteMax'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Configuration	Apparent Power (Max Charge)': {
    #         'mapped_points': ['702.VAChaRteMax'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Configuration	Voltage AC (nominal)': {
    #         'mapped_points': ['702.Vnom'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Configuration	Voltage AC (max)': {
    #         'mapped_points': [],
    #         'transform_type': 'exclude',
    #         'writable': False
    #     },
    #     'Configuration	Voltage AC (min)': {
    #         'mapped_points': [],
    #         'transform_type': 'exclude',
    #         'writable': False
    #     },
    #     'Configuration	Supported Control Mode Functions': {
    #         'mapped_points': [],
    #         'transform_type': 'exclude',
    #         'writable': False
    #     },
    #     'Configuration	Reactive Susceptance': {
    #         'mapped_points': [],
    #         'transform_type': 'exclude',
    #         'writable': False
    #     },
    #     'Configuration	Manufacturer': {
    #         'mapped_points': [],
    #         'transform_type': 'exclude',
    #         'writable': False
    #     },
    #     'Configuration	Model': {
    #         'mapped_points': [],
    #         'transform_type': 'exclude',
    #         'writable': False
    #     },
    #     'Configuration	Serial Number': {
    #         'mapped_points': [],
    #         'transform_type': 'exclude',
    #         'writable': False
    #     },
    #     'Configuration	Version': {
    #         'mapped_points': [],
    #         'transform_type': 'exclude',
    #         'writable': False
    #     },
    #     'Configuration	Storage Capacity': {
    #         'mapped_points': [],
    #         'transform_type': 'exclude',
    #         'writable': False
    #     },
    #     'Monitoring	Active Power': {
    #         'mapped_points': ['701.W'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Monitoring	Reactive Power': {
    #         'mapped_points': ['701.Var'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Monitoring	Voltage(s)': {
    #         'mapped_points': ['701.LLV', '701.LNV', '701.VL1L2', '701.VL1', '701.VL2L3', '701.VL2', '701.VL3L1', '701.VL3'],
    #         'transform_type': 'map_list',
    #         'writable': True
    #     },
    #     'Monitoring	Frequency': {
    #         'mapped_points': ['701.Hz'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Monitoring	Operation State': {
    #         'mapped_points': ['701.St'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Monitoring	Connection Status': {
    #         'mapped_points': ['701.ConnSt'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Monitoring	Alarm Status': {
    #         'mapped_points': ['701.Alrm'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Monitoring	Operation SoC': {
    #         'mapped_points': ['713.SoC'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Constant PF	Enable': {
    #         'mapped_points': ['704.PFWInjEna'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Constant PF	Injection/Absorption setting': {
    #         'mapped_points': ['704.PFWInj.PF'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Constant PF	Excitation setting': {
    #         'mapped_points': ['704.PFWInj.Ext'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Volt-VAR	Enable': {
    #         'mapped_points': ['705.Ena'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Volt-VAR	Vref ': {
    #         'mapped_points': ['705.VRef'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Volt-VAR	Autonomous Vref Adjustment enable': {
    #         'mapped_points': ['705.VRefAutoEna'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Volt-VAR	Vref Adjustment Time Constant': {
    #         'mapped_points': ['705.VRefAutoTms'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Volt-VAR	V/Q Curve Points': {
    #         'mapped_points': ['705.Crv.Pt[#].V', '705.Crv.Pt[#].Var'],
    #         'transform_type': 'map_curve',  # TODO: Implement a transform that can fill in the point names too.
    #         'writable': True
    #     },
    #     'Volt-VAR	Open Loop Response Time': {
    #         'mapped_points': ['705.RspTms'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Watt-VAR	Enable': {
    #         'mapped_points': ['712.Ena'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Watt-VAR	P/Q Curve Points': {
    #         'mapped_points': ['712.Crv.Pt[#].W', '712.Crv.Pt[#].Var'],
    #         'transform_type': 'map_curve',  # TODO: Implement a transform that can fill in the point names too.
    #         'writable': True
    #     },
    #     'Constant VAR	Enable': {
    #         'mapped_points': ['704.VarSetEna'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Constant VAR	VAR Setting': {
    #         'mapped_points': ['704.VarSetPct'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Volt-Watt	Enable': {
    #         'mapped_points': ['706.Ena'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Volt-Watt	V/P Curve Points': {
    #         'mapped_points': ['706.Crv.Pt[#].V', '706.Crv.Pt[#].W'],
    #         'transform_type': 'map_curve',  # TODO: Implement a transform that can fill in the point names too.
    #         'writable': True
    #     },
    #     'Volt-Watt	Open Loop Response Time': {
    #         'mapped_points': ['706.RspTms'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Voltage Trip	HV Trip Curve Points': {
    #         'mapped_points': ['707.MustTrip.Crv.Pt[#].V', '707.MustTrip.Crv.Pt[#].Tms'],
    #         'transform_type': 'map_curve',  # TODO: Implement a transform that can fill in the point names too.
    #         'writable': True
    #     },
    #     'Voltage Trip	LV Trip Curve Points': {
    #         'mapped_points': ['708.MustTrip.Crv.Pt[#].V', '708.MustTrip.Crv.Pt[#].Tms'],
    #         'transform_type': 'map_curve',  # TODO: Implement a transform that can fill in the point names too.
    #         'writable': True
    #     },
    #     'Momentary Cessation	HV Trip Curve Points': {
    #         'mapped_points': ['707.MomCess.Crv.Pt[#].V', '707.MomCess.Crv.Pt[#].Tms'],
    #         'transform_type': 'map_curve',  # TODO: Implement a transform that can fill in the point names too.
    #         'writable': True
    #     },
    #     'Momentary Cessation	LV Trip Curve Points': {
    #         'mapped_points': ['708.MomCess.Crv.Pt[#].V', '708.MomCess.Crv.Pt[#].Tms'],
    #         'transform_type': 'map_curve',  # TODO: Implement a transform that can fill in the point names too.
    #         'writable': True
    #     },
    #     'Frequency Trip	HV Trip Curve Points': {
    #         'mapped_points': ['709.MustTrip.Crv.Pt[#].Hz', '707.MustTrip.Crv.Pt[#].Tms'],
    #         'transform_type': 'map_curve',  # TODO: Implement a transform that can fill in the point names too.
    #         'writable': True
    #     },
    #     'Frequency Trip	LV Trip Curve Points': {
    #         'mapped_points': ['710.MustTrip.Crv.Pt[#].Hz', '710.MustTrip.Crv.Pt[#].Tms'],
    #         'transform_type': 'map_curve',  # TODO: Implement a transform that can fill in the point names too.
    #         'writable': True
    #     },
    #     'Frequency-Watt	dbof': {
    #         'mapped_points': ['711.Ctl.DbOf'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Frequency-Watt	dbuf': {
    #         'mapped_points': ['711.Ctl.DbUf'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Frequency-Watt	kof': {
    #         'mapped_points': ['711.Ctl.KOf'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Frequency-Watt	kuf': {
    #         'mapped_points': ['711.Ctl.Kuf'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Frequency-Watt	Open Loop Response Time': {
    #         'mapped_points': ['711.Ctl.RspTms'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Enter Service	Permit service': {
    #         'mapped_points': ['703.ES'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Enter Service	ES Voltage High': {
    #         'mapped_points': ['703.ESVHi'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Enter Service	ES Voltage Low': {
    #         'mapped_points': ['703.ESVLo'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Enter Service	ES Frequency High': {
    #         'mapped_points': ['703.ESHzHi'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Enter Service	ES Frequency Low': {
    #         'mapped_points': ['703.ESHzLo'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Enter Service	ES Delay': {
    #         'mapped_points': ['703.ESDlyTms'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Enter Service	ES Randomized Delay': {
    #         'mapped_points': ['703.ESRndTms'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Enter Service	ES Ramp Time': {
    #         'mapped_points': ['703.ESRmpTms'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Limit Watt	Enable': {
    #         'mapped_points': ['704.WMaxLimPctEna'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    #     'Limit Watt	Watt Setting': {
    #         'mapped_points': ['704.WMaxLimPct'],
    #         'transform_type': 'one_to_one',
    #         'writable': True
    #     },
    # }
