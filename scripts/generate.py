import argparse
import torch
import genesis as gs

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--vis", action="store_true", default=True)  # Changed default to True since you want visualization
    args = parser.parse_args()
    
    ########################## init ##########################
    gs.init(backend=gs.metal,
            theme='light',
            debug = True)
            
    ########################## create a scene ##########################
    scene = gs.Scene(
        show_viewer=args.vis,  # Use the command line argument
        viewer_options=gs.options.ViewerOptions(
            res=(1280, 960),
            camera_pos=(3.5, 0.0, 2.5),
            camera_lookat=(3.5, 0.0, 2.5),
            camera_fov=30,
            max_FPS=60,
        ),
        vis_options=gs.options.VisOptions(
            show_world_frame=True,
            world_frame_size=1.0,
            show_link_frame=False,
            show_cameras=True,
            plane_reflection=True,
            ambient_light=(0.1, 0.1, 0.1),
        ),
        renderer=gs.renderers.Rasterizer(),
    )   
    
    ########################## entities ##########################
    gs.generate("A fox jumps over the creek.")
    
    cam = scene.add_camera(
        res=(640, 480),
        pos=(3.5, 0.0, 2.5),
        lookat=(0, 0, 0.5),
        fov=30,
        GUI=True,
    )
    
    ########################## build ##########################
    scene.build()
    
    # Start simulation in separate thread
    sim_thread = gs.tools.run_in_another_thread(fn=run_sim, args=(scene, args.vis))
    
    # Only start viewer if visualization is enabled
    if args.vis:
        try:
            scene.viewer.start()
        except KeyboardInterrupt:
            print("Stopping simulation...")
            scene.viewer.stop()
            sim_thread.join()  # Wait for simulation thread to finish

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
            if i > 2e10:
                break
    except Exception as e:
        print(f"Simulation error: {e}")
    finally:
        if enable_vis:
            scene.viewer.stop()

if __name__ == "__main__":
    main()