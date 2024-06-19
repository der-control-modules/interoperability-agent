import logging
import sys

from typing import Dict, Iterable

from importlib.metadata import version
if int(version('volttron').split('.')[0]) >= 10:
    from volttron.client.vip.agent import Agent
    from volttron.client.vip.agent.subsystems.rpc import RPC
    from volttron.utils import setup_logging, vip_main
else:
    # noinspection PyUnresolvedReferences
    from volttron.platform.vip.agent import Agent, RPC
    # noinspection PyUnresolvedReferences
    from volttron.platform.agent.utils import setup_logging, vip_main

from .interoperable_target import InteroperableTarget

setup_logging()
_log = logging.getLogger(__name__)

__version__ = 0.1


class InteroperabilityAgent(Agent):
    def __init__(self, **kwargs):
        kwargs.pop('config_path')
        super(InteroperabilityAgent, self).__init__(**kwargs)
        self.default_config = {
        }
        self.vip.config.set_default("config", self.default_config)
        self.vip.config.subscribe(self.configure_main,
                                  actions=["NEW", "UPDATE"],
                                  pattern="config")
        self.targets = {}
        _log.debug(f'########## AT END OF INIT, TARGETS IS: {self.targets}')

    def configure_main(self, _, __, contents):
        _log.debug(f'####### IN CONFIGURE_MAIN, CONTENTS IS: {contents}')
        config = self.default_config.copy()
        _log.debug(f'####### IN CONFIGURE_MAIN, CONFIG STARTS: {config}')
        config.update(contents)
        _log.debug(f'####### IN CONFIGURE_MAIN, CONFIG BECOMES: {config}')
        for target_name, target_config in config.get('targets', {}).items():
            _log.debug(f"########## CONFIGURING: {target_name} WITH: {target_config}")
            self.targets[target_name] = InteroperableTarget.factory(self, target_config)
        _log.debug(f'########## AT END OF CONFIGURE_MAIN, TARGETS IS: {self.targets}')

    @RPC.export
    def get(self, target: str, point_names: Iterable):
        _log.debug(f'####### IN GET, TARGET IS: {target}, POINT_NAMES IS: {point_names}')

        return self.targets[target].get(point_names)

    @RPC.export
    def set(self, target: str, point_value_dict: Dict[str, any]):
        _log.debug(f'####### IN SET, TARGET IS: {target}, POINT_VALUE_DICT IS: {point_value_dict}')
        return self.targets[target].set(point_value_dict)

    @RPC.export
    def constant_pf_mode(self, target, enable, inject_absorption_setting, excitation_setting):
        _log.debug(f'####### IN CONSTANT_PF_MODE, TARGET IS: {target}, ENABLE IS: {enable}')
        return self.targets[target].constant_pf_mode(enable, inject_absorption_setting, excitation_setting)

    @RPC.export
    def volt_var_mode(self, target, enable, v_ref, autonomous_v_ref_adjustment_enable, v_ref_adjustment_time_constant,
                      v_q_curve_points, open_loop_response_time):
        return self.targets[target].volt_var_mode(
            enable, v_ref, autonomous_v_ref_adjustment_enable, v_ref_adjustment_time_constant, v_q_curve_points,
            open_loop_response_time)

    @RPC.export
    def watt_var_mode(self, target, enable, p_q_curve_points):
        return self.targets[target].watt_var_mode(enable, p_q_curve_points)

    @RPC.export
    def constant_var_mode(self, target, enable, var_setting):
        return self.targets[target].constant_var_mode(enable, var_setting)

    @RPC.export
    def volt_watt_mode(self, target, enable, v_p_curve_points, open_loop_response_time):
        return self.targets[target].volt_watt_mode(enable, v_p_curve_points, open_loop_response_time)

    @RPC.export
    def voltage_trip_mode(self, target, hv_trip_curve_points, lv_trip_curve_points):
        return self.targets[target].voltage_trip_mode(hv_trip_curve_points, lv_trip_curve_points)

    @RPC.export
    def momentary_cessation_mode(self, target, hv_trip_curve_points, lv_trip_curve_points):
        return self.targets[target].momentary_cessation_mode(hv_trip_curve_points, lv_trip_curve_points)

    @RPC.export
    def frequency_trip_mode(self,  target, hv_trip_curve_points, lv_trip_curve_points):
        return self.targets[target].frequency_trip_mode(hv_trip_curve_points, lv_trip_curve_points)

    @RPC.export
    def frequency_watt_mode(self, target, d_bof, d_buf, kof, kuf, open_loop_response_time):
        return self.targets[target].frequency_watt_mode(d_bof, d_buf, kof, kuf, open_loop_response_time)

    @RPC.export
    def enter_service(self, target, permit_service, es_voltage_high, es_voltage_low, es_frequency_high,
                      es_frequency_low, es_delay, es_randomized_delay, es_ramp_time):
        return self.targets[target].enter_service(permit_service, es_voltage_high, es_voltage_low, es_frequency_high,
                      es_frequency_low, es_delay, es_randomized_delay, es_ramp_time)

    @RPC.export
    def limit_watt_mode(self, target, enable, watt_setting):
        return self.targets[target].limit_watt_mode(enable, watt_setting)

def main():
    """Main method called by the app."""
    try:
        vip_main(InteroperabilityAgent)
    except Exception as exception:
        _log.exception("unhandled exception")
        _log.error(repr(exception))


if __name__ == "__main__":
    """Entry point for script"""
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        pass
