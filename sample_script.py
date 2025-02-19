import minedojo

env = minedojo.make(
    task_id="harvest_wool_with_shears_and_sheep",
    start_position=dict(x=-260, y=80, z=173, yaw=0, pitch=0),
    world_seed="MineDojo",
    image_size=(640, 1024)
)
obs = env.reset()
for i in range(1000):
    act = env.action_space.no_op()
    act[0] = 1    # forward/backward
    if i % 10 == 0:
        act[2] = 1    # jump
    obs, reward, done, info = env.step(act)
env.close()
