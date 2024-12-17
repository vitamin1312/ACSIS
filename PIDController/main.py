# from tclab import clock, setup, Historian, Plotter
# import tclab as tcl


# def PIDController(Kp, Ki, Kd, MV = 0):
#     e_param = 0
#     time_param = 10
#     KI = 0
#     M_Var = MV

#     while True:
#         yield M_Var
#         time, Point, SetPoint = None, tcl.T1, tcl.SP
#         error_val = SetPoint - Point
#         KP = Kp * error_val
#         KI = KI + Ki * error_val * (time - time_param)
#         KD = Kd * (error_val - e_param) / (time - time_param)
#         M_Var = MV + KP + KI + KD
#         e_param = error_val
#         time_param = time


# if __name__ == '__main__':
#     TCL = setup(connected=False, speedup=5)
#     controller = PIDController(1.5, 0, 0)
#     controller.send(None)
#     T_final = 200

#     with TCL() as tcl_var:
#         h = Historian([('SP', lambda: SP), ('T1', lambda: tcl.T1), ('MV', lambda: MV), ('Q1')])
#         Pl = Plotter(h, T_final)

#         T1 = tcl.T1

#         for time in clock(T_final, 2):
#             SetPoint = T1 if time < 150 else 150
#             Point = tcl.T1
#             MV = controller.send([time, Point, SetPoint])
#             tcl.U1 = MV


def f(number):
    while True:
        number * 2
        number = yield number

fun = f(4)
print(fun.send(3))
print(next(fun))