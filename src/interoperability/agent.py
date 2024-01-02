from collections import defaultdict

from volttron.client.vip.agent import Agent
from volttron.client.vip.agent.subsystems.rpc import RPC


class TargetData:
    def __init__(self):
        self.nameplate = Nameplate
        self.configuration = Configuration
        self.monitoring = Monitoring

    @classmethod
    def factory(cls, config):
        pass


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
        #TODO: Containers/Classes for nameplate, configuration, and monitoring.

    def configure_main(self, config_name, action, contents):
        config = self.default_config.copy()
        config.update(contents)
        for target_config in config.get('targets', {}):
            self.targets = TargetData.factory(target_config)

    @RPC.export
    def constant_pf_mode(self, target, enable, inject_absorption_setting, excitation_setting):
        pass

    @RPC.export
    def volt_var_mode(self, target, enable, v_ref, autonomous_v_ref_adjustment_enable, v_ref_adjustment_time_constant,
                      v_q_curve_points, open_loop_response_time):
        pass

    @RPC.export
    def watt_var_mode(self, target, enable, p_q_curve_points):
        pass

    @RPC.export
    def constant_var_mode(self, target, enable, var_setting):
        pass

    @RPC.export
    def volt_watt_mode(self, target, enable, v_p_curve_points, open_loop_response_time):
        pass

    @RPC.export
    def voltage_trip_mode(self, target, hv_trip_curve_points, lv_trip_curve_points):
        pass

    @RPC.export
    def momentary_cessation_mode(self, target, hv_trip_curve_points, lv_trip_curve_points):
        pass

    @RPC.export
    def frequency_trip_mode(self,  target, hv_trip_curve_points, lv_trip_curve_points):
        pass

    @RPC.export
    def frequency_watt_mode(self, target, dbof, dbuf, kof, kuf, open_loop_response_time):
        pass

    @RPC.export
    def enter_service(self, target, permit_service, es_volttage_high, es_volttage_low, es_frequency_high,
                      es_frequency_low, es_delay, es_randomized_delay, es_ramp_time):
        pass

    @RPC.export
    def limit_watt_mode(self, target, enable, watt_setting):
        pass
