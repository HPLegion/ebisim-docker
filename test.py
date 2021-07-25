#!/usr/local/bin/python
import ebisim as eb
import pickle

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