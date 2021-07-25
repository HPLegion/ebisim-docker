#!/usr/local/bin/python

# import logging

# class FilterModule(logging.Filter):
#     def __init__(self, modulename=""):
#         self.modulename = modulename
#     def filter(self, rec):
#         return rec.name.startswith(self.modulename)

# logging.basicConfig()
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)
# for handler in logger.handlers:
#     handler.addFilter(FilterModule("ebisim"))


import ebisim as eb
import pickle

if __name__ == "__main__":
    device = eb.Device.get(
        current = 0.2,
        e_kin = 6000.0,
        r_e = 150e-6,
        v_ax = 1000.0,
        b_ax = 2.0,
        r_dt = 5e-3,
    )

    target = eb.Element.get_ions(
        element_id = "Potassium",
        nl = 1e6,
        kT = 5,
    )

    options = eb.ModelOptions(
        RADIAL_DYNAMICS = True,
        RECOMPUTE_CROSS_SECTIONS = True
    )

    t_max = 0.1

    sol = eb.advanced_simulation(device, target, t_max, options=options, rates=True)

    with open("test_output.pickle", "wb") as f:
        pickle.dump(sol, f)

    exit()
