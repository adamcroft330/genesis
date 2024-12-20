import argparse

import numpy as np

import genesis as gs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--vis", action="store_true", default=False)
    args = parser.parse_args()

    ########################## init ##########################
    gs.init(backend=gs.metal,
        theme='light',
        debug = True)

    ########################## create a scene ##########################
    viewer_options = gs.options.ViewerOptions(
        camera_pos=(3, -1, 1.5),
        camera_lookat=(0.0, 0.0, 0.0),
        camera_fov=30,
        max_FPS=60,
    )

    scene = gs.Scene(
        viewer_options=viewer_options,
        rigid_options=gs.options.RigidOptions(
            dt=0.01,
        ),
        show_viewer=args.vis,
    )

    ########################## entities ##########################
    plane = scene.add_entity(
        gs.morphs.URDF(file="urdf/plane/plane.urdf", fixed=True),
    )
    bottle = scene.add_entity(
        material=gs.materials.Rigid(rho=300),
        morph=gs.morphs.URDF(
            file="urdf/3763/mobility_vhacd.urdf",
            scale=0.09,
            pos=(0.65, 0.0, 0.036),
            euler=(0, 90, 0),
        ),
      
    )
    franka = scene.add_entity(
        gs.morphs.MJCF(file="xml/franka_emika_panda/panda.xml"),
    )
    # Define DOF indices for the robot
    motors_dof = list(range(7))  # Arm joints 0-6
    fingers_dof = list(range(7, 9))  # Gripper joints 7-8

    cam = scene.add_camera(
        res    = (640, 480),
        pos    = (3.5, 0.0, 2.5),
        lookat = (0, 0, 0.5),
        fov    = 30,
        GUI    = True,
    )
    ########################## build ##########################
    scene.build()
    
    ########################## start cam recording ########################## 
    cam.start_recording()

    cam.render() 

    # Optional: set control gains
    franka.set_dofs_kp(
        np.array([4500, 4500, 3500, 3500, 2000, 2000, 2000, 100, 100]),
    )
    franka.set_dofs_kv(
        np.array([450, 450, 350, 350, 200, 200, 200, 10, 10]),
    )
    franka.set_dofs_force_range(
        np.array([-87, -87, -87, -87, -12, -12, -12, -100, -100]),
        np.array([87, 87, 87, 87, 12, 12, 12, 100, 100]),
    )

    end_effector = franka.get_link("hand")

    # move to pre-grasp pose
    qpos = franka.inverse_kinematics(
        link=end_effector,
        pos=np.array([0.65, 0.0, 0.25]),
        quat=np.array([0, 1, 0, 0]),
    )
    qpos[-2:] = 0.04
    path = franka.plan_path(qpos)
    for waypoint in path:
        franka.control_dofs_position(waypoint)
        scene.step()
        cam.render()    # Render frame for each motion step

    # reach
    qpos = franka.inverse_kinematics(
        link=end_effector,
        pos=np.array([0.65, 0.0, 0.142]),
        quat=np.array([0, 1, 0, 0]),
    )
    franka.control_dofs_position(qpos[:-2], motors_dof)
    for i in range(100):
        scene.step()
        cam.render()

    # grasp
    franka.control_dofs_position(qpos[:-2], motors_dof)
    franka.control_dofs_position(np.array([0, 0]), fingers_dof)  # you can use position control
    for i in range(100):
        scene.step()
        cam.render()

    # lift
    qpos = franka.inverse_kinematics(
        link=end_effector,
        pos=np.array([0.65, 0.0, 0.3]),
        quat=np.array([0, 1, 0, 0]),
    )
    franka.control_dofs_position(qpos[:-2], motors_dof)
    franka.control_dofs_force(np.array([-20, -20]), fingers_dof)  # can also use force control
    for i in range(100):
        scene.step()
        cam.render()
    print("Lift complete, stopping recording")
    
    # Stop recording at the very end of your simulation
    cam.stop_recording(save_to_filename='grasp_waterbottle_video.mp4', fps=60)

def run_sim(scene, enable_vis):
    from time import time
    t_prev = time()
    i = 0
    try:
        while True:
            i += 1
            scene.step()
            t_now = time()
            print(1 / (t_now - t_prev), "FPS")
            t_prev = t_now
            if i > 1000:
                break
    except Exception as e:
        print(f"Simulation error: {e}")
    finally:
        if enable_vis:
            scene.viewer.stop()

if __name__ == "__main__":
    main()