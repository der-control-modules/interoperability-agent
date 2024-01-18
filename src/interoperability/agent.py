from typing import Iterable
from volttron.client.vip.agent import Agent
from volttron.client.vip.agent.subsystems.rpc import RPC

from .interoperable_target import InteroperableTarget


class InteroperabilityAgent(Agent):
    def __init__(self):
        super(InteroperabilityAgent, self).__init__()
        self.default_config = {
        }
        self.vip.config.set_default("config", self.default_config)
        self.vip.config.subscribe(self.configure_main,
                                  actions=["NEW", "UPDATE"],
                                  pattern="config")
        self.targets = {}

    def configure_main(self, config_name, action, contents):
        config = self.default_config.copy()
        config.update(contents)
        for target_config in config.get('targets', {}):
            self.targets = InteroperableTarget.factory(target_config)

    @RPC.export
    def get(self, target: str, point_names: Iterable):
        return self.targets[target].get(point_names)

    @RPC.export
    def set(self, target: str, point_value_dict: dict[str, any]):
        return self.targets[target].set(point_value_dict)

    @RPC.export
    def constant_pf_mode(self, target, enable, inject_absorption_setting, excitation_setting):
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
    def frequency_watt_mode(self, target, dbof, dbuf, kof, kuf, open_loop_response_time):
        return self.targets[target].frequency_watt_mode(dbof, dbuf, kof, kuf, open_loop_response_time)

    @RPC.export
    def enter_service(self, target, permit_service, es_volttage_high, es_volttage_low, es_frequency_high,
                      es_frequency_low, es_delay, es_randomized_delay, es_ramp_time):
        return self.targets[target].enter_service(permit_service, es_volttage_high, es_volttage_low, es_frequency_high,
                      es_frequency_low, es_delay, es_randomized_delay, es_ramp_time)

    @RPC.export
    def limit_watt_mode(self, target, enable, watt_setting):
        return self.targets[target].limit_watt_mode(enable, watt_setting)
