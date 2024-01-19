from typing import Iterable

from interoperability.interoperable_target import InteroperableTarget


class SunSpecModbus(InteroperableTarget):
    def __init__(self, **kwargs):
        super(SunSpecModbus, self).__init__(**kwargs)

    # TODO: Implement
    def poll_values(self, point_names: Iterable) -> bool:
        pass

    # TODO: Implement
    def set_values(self, request_dict: dict[str, any]) -> bool:
        pass

    MAPPING = {
        'Nameplate	Active Power (unity)': {
            'mapped_points': ['702.WMaxRtg'],
            'transform_type': 'one_to_one',
            'writable': False
        },
        'Nameplate	Active Power (over-excited)': {
            'mapped_points': ['702.WOvrExtRtg'],
            'transform_type': 'one_to_one',
            'writable': False
        },
        'Nameplate	Power Factor (over-excited)': {
            'mapped_points': ['702.WOvrExtRtgPF'],
            'transform_type': 'one_to_one',
            'writable': False
        },
        'Nameplate	Active Power (under-excited)': {
            'mapped_points': ['702.WUndExtRtg'],
            'transform_type': 'one_to_one',
            'writable': False
        },
        'Nameplate	Power Factor (under-excited)': {
            'mapped_points': ['702.WUndExtRtgPF'],
            'transform_type': 'one_to_one',
            'writable': False
        },
        'Nameplate	Apparent Power (Max)': {
            'mapped_points': ['702.VAMaxRtg'],
            'transform_type': 'one_to_one',
            'writable': False
        },
        'Nameplate	Normal (operating category)': {
            'mapped_points': ['702.NorOpCatRtg'],
            'transform_type': 'one_to_one',
            'writable': False
        },
        'Nameplate	Abnormal (operating category)': {
            'mapped_points': ['702.AbnOpCatRtg'],
            'transform_type': 'one_to_one',
            'writable': False
        },
        'Nameplate	Reactive Power (Max Injected)': {
            'mapped_points': ['702.VarMaxInjRtg'],
            'transform_type': 'one_to_one',
            'writable': False
        },
        'Nameplate	Reactive Power (Max Absorbed)': {
            'mapped_points': ['702.VarMaxIAbsRtg'],
            'transform_type': 'one_to_one',
            'writable': False
        },
        'Nameplate	Active Power (Max Charge)': {
            'mapped_points': ['702.WChaRteMaxRtg'],
            'transform_type': 'one_to_one',
            'writable': False
        },
        'Nameplate	Apparent Power (Max Charge)': {
            'mapped_points': ['702.WChaRteMaxRtg'],
            'transform_type': 'one_to_one',
            'writable': False
        },
        'Nameplate	Voltage AC (nominal)': {
            'mapped_points': ['702.VNomRtg'],
            'transform_type': 'one_to_one',
            'writable': False
        },
        'Nameplate	Voltage AC (max)': {
            'mapped_points': ['702.VMaxRtg'],
            'transform_type': 'one_to_one',
            'writable': False
        },
        'Nameplate	Voltage AC (min)': {
            'mapped_points': ['702.VMinRtg'],
            'transform_type': 'one_to_one',
            'writable': False
        },
        'Nameplate	Supported Control Mode Functions': {
            'mapped_points': ['702.CtrlModes'],
            'transform_type': 'one_to_one',
            'writable': False
        },
        'Nameplate	Reactive Susceptance': {
            'mapped_points': ['702.ReactSusceptRtg'],
            'transform_type': 'one_to_one',
            'writable': False
        },
        'Nameplate	Manufacturer': {
            'mapped_points': ['1.Mn'],
            'transform_type': 'one_to_one',
            'writable': False
        },
        'Nameplate	Model': {
            'mapped_points': ['1.Md'],
            'transform_type': 'one_to_one',
            'writable': False
        },
        'Nameplate	Serial Number': {
            'mapped_points': ['1.SN'],
            'transform_type': 'one_to_one',
            'writable': False
        },
        'Nameplate	Version': {
            'mapped_points': ['1.Vr'],
            'transform_type': 'one_to_one',
            'writable': False
        },
        'Nameplate	Storage Capacity': {
            'mapped_points': [],
            'transform_type': 'exclude',
            'writable': False
        },
        'Configuration	Active Power (unity)': {
            'mapped_points': ['702.Wmax'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Configuration	Active Power (over-excited)': {
            'mapped_points': ['702.WMaxOvrExt'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Configuration	Power Factor (over-excited)': {
            'mapped_points': ['702.WOvrExtPF'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Configuration	Active Power (under-excited)': {
            'mapped_points': ['702.WMaxUndExt'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Configuration	Power Factor (under-excited)': {
            'mapped_points': ['702.WUndExtPF'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Configuration	Apparent Power (Max)': {
            'mapped_points': ['702.VAMax'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Configuration	Normal (operating category)': {
            'mapped_points': ['702.IntIslandCat'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Configuration	Abnormal (operating category)': {
            'mapped_points': [],
            'transform_type': 'exclude',
            'writable': False
        },
        'Configuration	Reactive Power (Max Injected)': {
            'mapped_points': ['702.VarMaxInjRtg'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Configuration	Reactive Power (Max Absorbed)': {
            'mapped_points': ['702.VarMaxAbsRtg'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Configuration	Active Power (Max Charge)': {
            'mapped_points': ['702.WChaRteMax'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Configuration	Apparent Power (Max Charge)': {
            'mapped_points': ['702.VAChaRteMax'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Configuration	Voltage AC (nominal)': {
            'mapped_points': ['702.Vnom'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Configuration	Voltage AC (max)': {
            'mapped_points': [],
            'transform_type': 'exclude',
            'writable': False
        },
        'Configuration	Voltage AC (min)': {
            'mapped_points': [],
            'transform_type': 'exclude',
            'writable': False
        },
        'Configuration	Supported Control Mode Functions': {
            'mapped_points': [],
            'transform_type': 'exclude',
            'writable': False
        },
        'Configuration	Reactive Susceptance': {
            'mapped_points': [],
            'transform_type': 'exclude',
            'writable': False
        },
        'Configuration	Manufacturer': {
            'mapped_points': [],
            'transform_type': 'exclude',
            'writable': False
        },
        'Configuration	Model': {
            'mapped_points': [],
            'transform_type': 'exclude',
            'writable': False
        },
        'Configuration	Serial Number': {
            'mapped_points': [],
            'transform_type': 'exclude',
            'writable': False
        },
        'Configuration	Version': {
            'mapped_points': [],
            'transform_type': 'exclude',
            'writable': False
        },
        'Configuration	Storage Capacity': {
            'mapped_points': [],
            'transform_type': 'exclude',
            'writable': False
        },
        'Monitoring	Active Power': {
            'mapped_points': ['701.W'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Monitoring	Reactive Power': {
            'mapped_points': ['701.Var'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Monitoring	Voltage(s)': {
            'mapped_points': ['701.LLV', '701.LNV', '701.VL1L2', '701.VL1', '701.VL2L3', '701.VL2', '701.VL3L1', '701.VL3'],
            'transform_type': 'map_list',
            'writable': True
        },
        'Monitoring	Frequency': {
            'mapped_points': ['701.Hz'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Monitoring	Operation State': {
            'mapped_points': ['701.St'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Monitoring	Connection Status': {
            'mapped_points': ['701.ConnSt'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Monitoring	Alarm Status': {
            'mapped_points': ['701.Alrm'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Monitoring	Operation SoC': {
            'mapped_points': ['713.SoC'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Constant PF	Enable': {
            'mapped_points': ['704.PFWInjEna'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Constant PF	Injection/Absorption setting': {
            'mapped_points': ['704.PFWInj.PF'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Constant PF	Excitation setting': {
            'mapped_points': ['704.PFWInj.Ext'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Volt-VAR	Enable': {
            'mapped_points': ['705.Ena'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Volt-VAR	Vref ': {
            'mapped_points': ['705.VRef'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Volt-VAR	Autonomous Vref Adjustment enable': {
            'mapped_points': ['705.VRefAutoEna'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Volt-VAR	Vref Adjustment Time Constant': {
            'mapped_points': ['705.VRefAutoTms'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Volt-VAR	V/Q Curve Points': {
            'mapped_points': ['705.Crv.Pt[#].V', '705.Crv.Pt[#].Var'],
            'transform_type': 'map_curve',  # TODO: Implement a transform that can fill in the point names too.
            'writable': True
        },
        'Volt-VAR	Open Loop Response Time': {
            'mapped_points': ['705.RspTms'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Watt-VAR	Enable': {
            'mapped_points': ['712.Ena'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Watt-VAR	P/Q Curve Points': {
            'mapped_points': ['712.Crv.Pt[#].W', '712.Crv.Pt[#].Var'],
            'transform_type': 'map_curve',  # TODO: Implement a transform that can fill in the point names too.
            'writable': True
        },
        'Constant VAR	Enable': {
            'mapped_points': ['704.VarSetEna'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Constant VAR	VAR Setting': {
            'mapped_points': ['704.VarSetPct'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Volt-Watt	Enable': {
            'mapped_points': ['706.Ena'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Volt-Watt	V/P Curve Points': {
            'mapped_points': ['706.Crv.Pt[#].V', '706.Crv.Pt[#].W'],
            'transform_type': 'map_curve',  # TODO: Implement a transform that can fill in the point names too.
            'writable': True
        },
        'Volt-Watt	Open Loop Response Time': {
            'mapped_points': ['706.RspTms'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Voltage Trip	HV Trip Curve Points': {
            'mapped_points': ['707.MustTrip.Crv.Pt[#].V', '707.MustTrip.Crv.Pt[#].Tms'],
            'transform_type': 'map_curve',  # TODO: Implement a transform that can fill in the point names too.
            'writable': True
        },
        'Voltage Trip	LV Trip Curve Points': {
            'mapped_points': ['708.MustTrip.Crv.Pt[#].V', '708.MustTrip.Crv.Pt[#].Tms'],
            'transform_type': 'map_curve',  # TODO: Implement a transform that can fill in the point names too.
            'writable': True
        },
        'Momentary Cessation	HV Trip Curve Points': {
            'mapped_points': ['707.MomCess.Crv.Pt[#].V', '707.MomCess.Crv.Pt[#].Tms'],
            'transform_type': 'map_curve',  # TODO: Implement a transform that can fill in the point names too.
            'writable': True
        },
        'Momentary Cessation	LV Trip Curve Points': {
            'mapped_points': ['708.MomCess.Crv.Pt[#].V', '708.MomCess.Crv.Pt[#].Tms'],
            'transform_type': 'map_curve',  # TODO: Implement a transform that can fill in the point names too.
            'writable': True
        },
        'Frequency Trip	HV Trip Curve Points': {
            'mapped_points': ['709.MustTrip.Crv.Pt[#].Hz', '707.MustTrip.Crv.Pt[#].Tms'],
            'transform_type': 'map_curve',  # TODO: Implement a transform that can fill in the point names too.
            'writable': True
        },
        'Frequency Trip	LV Trip Curve Points': {
            'mapped_points': ['710.MustTrip.Crv.Pt[#].Hz', '710.MustTrip.Crv.Pt[#].Tms'],
            'transform_type': 'map_curve',  # TODO: Implement a transform that can fill in the point names too.
            'writable': True
        },
        'Frequency-Watt	dbof': {
            'mapped_points': ['711.Ctl.DbOf'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Frequency-Watt	dbuf': {
            'mapped_points': ['711.Ctl.DbUf'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Frequency-Watt	kof': {
            'mapped_points': ['711.Ctl.KOf'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Frequency-Watt	kuf': {
            'mapped_points': ['711.Ctl.Kuf'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Frequency-Watt	Open Loop Response Time': {
            'mapped_points': ['711.Ctl.RspTms'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Enter Service	Permit service': {
            'mapped_points': ['703.ES'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Enter Service	ES Voltage High': {
            'mapped_points': ['703.ESVHi'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Enter Service	ES Voltage Low': {
            'mapped_points': ['703.ESVLo'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Enter Service	ES Frequency High': {
            'mapped_points': ['703.ESHzHi'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Enter Service	ES Frequency Low': {
            'mapped_points': ['703.ESHzLo'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Enter Service	ES Delay': {
            'mapped_points': ['703.ESDlyTms'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Enter Service	ES Randomized Delay': {
            'mapped_points': ['703.ESRndTms'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Enter Service	ES Ramp Time': {
            'mapped_points': ['703.ESRmpTms'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Limit Watt	Enable': {
            'mapped_points': ['704.WMaxLimPctEna'],
            'transform_type': 'one_to_one',
            'writable': True
        },
        'Limit Watt	Watt Setting': {
            'mapped_points': ['704.WMaxLimPct'],
            'transform_type': 'one_to_one',
            'writable': True
        },
    }
