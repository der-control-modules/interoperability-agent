from typing import Iterable

from interoperability.interoperable_target import InteroperableTarget


class IEC_61850_7_420(InteroperableTarget):
    def __init__(self, **kwargs):
        super(IEC_61850_7_420, self).__init__(**kwargs)

    def get_values(self, point_names: Iterable) -> bool:
        pass

    def set_values(self, request_dict: dict[str, any]) -> bool:
        pass

    MAPPING = {
        'Nameplate Active Power (unity)': {
            'mapped_points': ['DGEN.WMaxRtg'],
            'transform_type': 'one_to_one',
            'writable': False},
        'Nameplate Active Power (over-excited)': {
            'mapped_points': ['DGEN.WGnOvPFRtg'],
            'transform_type': 'one_to_one',
            'writable': False},
        'Nameplate Power Factor (over-excited)': {
            'mapped_points': ['DGEN.OvPFRtg'],
            'transform_type': 'one_to_one',
            'writable': False},
        'Nameplate Active Power (under-excited)': {
            'mapped_points': ['DGEN.WGnUnPFRtg'],
            'transform_type': 'one_to_one',
            'writable': False},
        'Nameplate Power Factor (under-excited)': {
            'mapped_points': ['DGEN.UnPFRtg'],
            'transform_type': 'one_to_one',
            'writable': False},
        'Nameplate Apparent Power (Max)': {
            'mapped_points': ['DGEN.VAMaxRtg'],
            'transform_type': 'one_to_one',
            'writable': False},
        'Nameplate Normal (operating category)': {
            'mapped_points': ['DGEN.Ieee1547Cat1'],
            'transform_type': 'one_to_one',
            'writable': False},
        'Nameplate Abnormal (operating category)': {
            'mapped_points': ['DGEN.Ieee1547Cat2'],
            'transform_type': 'one_to_one',
            'writable': False},
        'Nameplate Reactive Power (Max Injected)': {
            'mapped_points': ['DGEN.VarMaxSupRtg'],
            'transform_type': 'one_to_one',
            'writable': False},
        'Nameplate Reactive Power (Max Absorbed)': {
            'mapped_points': ['DGEN.VarMaxAbgRtg'],
            'transform_type': 'one_to_one',
            'writable': False},
        'Nameplate Active Power (Max Charge)': {
            'mapped_points': ['DSTO.WChaUnPFRtg'],
            'transform_type': 'one_to_one',
            'writable': False},
        'Nameplate Apparent Power (Max Charge)': {
            'mapped_points': ['DSTO.VAMaxChaRtg'],
            'transform_type': 'one_to_one',
            'writable': False},
        'Nameplate Voltage AC (nominal)': {
            'mapped_points': ['DECP.VRef'],
            'transform_type': 'one_to_one',
            'writable': False},
        'Nameplate Voltage AC (max)': {
            'mapped_points': ['DGEN.VMaxRtg'],
            'transform_type': 'one_to_one',
            'writable': False},
        'Nameplate Voltage AC (min)': {
            'mapped_points': ['DGEN.VMinRtg'],
            'transform_type': 'one_to_one',
            'writable': False},
        'Nameplate Supported Control Mode Functions': {
            'mapped_points': ['DVRT', 'DFRT', 'DFWP', 'DWLM', 'DVWC', 'DFWC', 'DVAR', 'DFPF', 'DVVC', 'DWVR'],
            'transform_type': 'map_list',
            'writable': False},
        'Nameplate Reactive Susceptance': {
            'mapped_points': ['DGEN.SuscRtg'],
            'transform_type': 'one_to_one',
            'writable': False},
        'Nameplate Manufacturer': {
            'mapped_points': ['LPHD.PhyNam.vendor'],
            'transform_type': 'one_to_one',
            'writable': False},
        'Nameplate Model': {
            'mapped_points': ['LPHD.PhyNam.model'],
            'transform_type': 'one_to_one',
            'writable': False},
        'Nameplate Serial Number': {
            'mapped_points': ['LPHD.PhyNam.serNum'],
            'transform_type': 'one_to_one',
            'writable': False},
        'Nameplate Version': {
            'mapped_points': ['LPHD.PhyNam.swRev'],
            'transform_type': 'one_to_one',
            'writable': False},
        'Nameplate Storage Capacity': {
            'mapped_points': ['DSTO.WhRtg'],
            'transform_type': 'one_to_one',
            'writable': False},
        'Configuration Active Power (unity)': {
            'mapped_points': ['DGEN.Wmax'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Configuration Active Power (over-excited)': {
            'mapped_points': ['DGEN.WGnOvPFRtg'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Configuration Power Factor (over-excited)': {
            'mapped_points': ['DGEN.OvPFRtg'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Configuration Active Power (under-excited)': {
            'mapped_points': ['DGEN.WGnUnPFRtg'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Configuration Power Factor (under-excited)': {
            'mapped_points': ['DGEN.UnPFRtg'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Configuration Apparent Power (Max)': {
            'mapped_points': ['DGEN.VAMax'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Configuration Normal (operating category)': {
            'mapped_points': ['DGEN.RegCap'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Configuration Abnormal (operating category)': {
            'mapped_points': ['DGEN.RegCap'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Configuration Reactive Power (Max Injected)': {
            'mapped_points': ['DGEN.VarMaxSupRtg'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Configuration Reactive Power (Max Absorbed)': {
            'mapped_points': ['DGEN.VarMaxAbgRtg'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Configuration Active Power (Max Charge)': {
            'mapped_points': ['DSTO.WChaUnPFRtg'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Configuration Apparent Power (Max Charge)': {
            'mapped_points': ['DSTO.VAMaxChaRtg'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Configuration Voltage AC (nominal)': {
            'mapped_points': ['DECP.VRef'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Configuration Voltage AC (max)': {
            'mapped_points': ['DGEN.Vmax'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Configuration Voltage AC (min)': {
            'mapped_points': ['DGEN.Vmin'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Configuration Supported Control Mode Functions': {
            'mapped_points': ['DVRT', 'DFRT', 'DFWP', 'DWLM', 'DVWC', 'DFWC', 'DVAR', 'DFPF', 'DVVC', 'DWVR'],
            'transform_type': 'map_list',
            'writable': False},
        'Configuration Reactive Susceptance': {
            'mapped_points': ['DGEN.SuscRtg'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Configuration Manufacturer': {
            'mapped_points': ['LPHD.PhyNam.vendor'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Configuration Model': {
            'mapped_points': ['LPHD.PhyNam.model'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Configuration Serial Number': {
            'mapped_points': ['LPHD.PhyNam.serNum'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Configuration Version': {
            'mapped_points': ['LPHD.PhyNam.swRev'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Configuration Storage Capacity': {
            'mapped_points': ['DSTO.WhRtg'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Monitoring Active Power': {
            'mapped_points': ['DECP.MMXU.TotW'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Monitoring Reactive Power': {
            'mapped_points': ['DECP.MMXU.TotVAr'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Monitoring Voltage(s)': {
            'mapped_points': ['DECP.MMXU.PhV.phsA.mag, DECP.MMXU.PhV.phsB.mag, DECP.MMXU.PhV.phsC.mag'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Monitoring Frequency': {
            'mapped_points': ['DECP.MMXU.Hz'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Monitoring Operation State': {
            'mapped_points': ['DGEN.DERState'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Monitoring Connection Status': {
            'mapped_points': ['DSTO.DERState.1'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Monitoring Alarm Status': {
            'mapped_points': ['CALH.GrAlm'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Monitoring Operation SoC': {
            'mapped_points': ['DSTO.SocUsePct'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Constant PF Enable': {
            'mapped_points': ['DFPF.ModEna'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Constant PF Injection/Absorption setting': {
            'mapped_points': ['DFPF.PFGnTgt, DFPF.PFLodTgt'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Constant PF Excitation setting': {
            'mapped_points': ['DFPF.PFExtSet'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Volt-VAR Enable': {
            'mapped_points': ['DVVR.ModEna'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Volt-VAR Vref ': {
            'mapped_points': ['DECP.VRef'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Volt-VAR Autonomous Vref Adjustment enable': {
            'mapped_points': ['DECP.VRefOfs'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Volt-VAR Vref Adjustment Time Constant': {
            'mapped_points': ['DVVR.VRefTmms'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Volt-VAR V/Q Curve Points': {
            'mapped_points': ['DVVR.VVArCrv'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Volt-VAR Open Loop Response Time': {
            'mapped_points': ['DVVR.OpnLoopMax'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Watt-VAR Enable': {
            'mapped_points': ['DWVR.ModEna'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Watt-VAR P/Q Curve Points': {
            'mapped_points': ['DWVR.WVArCrv'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Constant VAR Enable': {
            'mapped_points': ['DVAR.ModEna'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Constant VAR VAR Setting': {
            'mapped_points': ['DVAR.VArTgt'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Volt-Watt Enable': {
            'mapped_points': ['DVWC.ModEna'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Volt-Watt V/P Curve Points': {
            'mapped_points': ['DVWC.VWCrv'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Volt-Watt Open Loop Response Time': {
            'mapped_points': ['DVWC.OpnLoopMax'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Voltage Trip HV Trip Curve Points': {
            'mapped_points': ['DHVT.TrZnSt, PTOV.TmVCrv'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Voltage Trip LV Trip Curve Points': {
            'mapped_points': ['DLVT.TrZnSt, PTUV.TmVCrv'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Momentary Cessation HV Trip Curve Points': {
            'mapped_points': ['DHVT.CeaZnSt, PTOV.TmVCrv'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Momentary Cessation LV Trip Curve Points': {
            'mapped_points': ['DLVT.CeaZnSt, PTUV.TmVCrv'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Frequency Trip HV Trip Curve Points': {
            'mapped_points': ['DHFT.TrZnSt, PTOF.StrVal'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Frequency Trip LV Trip Curve Points': {
            'mapped_points': ['DLFT.TrZnSt, PTUF.StrVal'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Frequency-Watt dbof': {
            'mapped_points': ['DHFW.HzStr'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Frequency-Watt dbuf': {
            'mapped_points': ['DLFW.HzStr'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Frequency-Watt kof': {
            'mapped_points': ['DHFW.WGra'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Frequency-Watt kuf': {
            'mapped_points': ['DLFW.WGra'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Frequency-Watt Open Loop Response Time': {
            'mapped_points': ['DHFW.OpnLoopMax, DLFW.OpnLoopMax'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Enter Service Permit service': {
            'mapped_points': ['DCTE.RtnSrvAuto, DCTE.RtnSrvAuth'],
            'transform_type': 'broadcast',
            'writable': True},
        'Enter Service ES Voltage High': {
            'mapped_points': ['DCTE.VHiLim'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Enter Service ES Voltage Low': {
            'mapped_points': ['DCTE.VLoLim'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Enter Service ES Frequency High': {
            'mapped_points': ['DCTE.HzHiLim'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Enter Service ES Frequency Low': {
            'mapped_points': ['DCTE.HzLoLim'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Enter Service ES Delay': {
            'mapped_points': ['DCTE.RtnSrvDlyTim'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Enter Service ES Randomized Delay': {
            'mapped_points': ['DCTE.RtnSrvDlyTim'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Enter Service ES Ramp Time': {
            'mapped_points': ['DCTE.RtnSrvRmpTim'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Limit Watt Enable': {
            'mapped_points': ['DWMX.ModEna, DWMN.ModEna'],
            'transform_type': 'one_to_one',
            'writable': True},
        'Limit Watt Watt Setting': {
            'mapped_points': ['DWMX.LimW', 'DWMN.LimW'],
            'transform_type': '',
            'writable': True}
    }
