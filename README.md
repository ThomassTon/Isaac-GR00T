# MAV × Isaac GR00T

This repository is a fork of NVIDIA Isaac GR00T. For the upstream documentation (installation, model checkpoints, general inference and evaluation workflow), read [`README_GR00T.md`](README_GR00T.md) first.

**Training scripts and the full finetuning workflow for our robot live in [`examples/MAV_handsover/README.md`](examples/MAV_handsover/README.md).**

## What this is

Isaac GR00T N1.6 is an open vision-language-action (VLA) model: it takes camera images, robot state and a language instruction, and outputs continuous action chunks. The pretrained 3B checkpoint ([`nvidia/GR00T-N1.6-3B`](https://huggingface.co/nvidia/GR00T-N1.6-3B)) is used as a base model, and we post-train it on our own robot data with the `MAV` embodiment tag.

The workflow is:

1. Collect demonstrations by teleoperating the robot.
2. Convert/record them in the GR00T-flavored LeRobot v2 format and drop the matching `modality.json` at the dataset root.
3. Finetune the base checkpoint on that dataset.
4. Evaluate open-loop against the dataset, then closed-loop on the real robot through the policy server.

## Data collection via teleoperation

Data is collected by teleoperating the follower arm with a leader arm, following the LeRobot teleoperation guide: https://huggingface.co/docs/lerobot/il_robots

### Also record imperfect episodes

Do **not** record only clean, first-try successes. A policy trained purely on perfect demonstrations never learns what to do once something goes wrong, so at test time a single mis-grasp ends the episode.

Deliberately include recovery behaviour in the dataset, for example:

- The first grasp misses or the object slips out of the gripper — reopen the gripper, back off, re-approach and grasp again in the same episode.
- The object is picked up at a bad angle — put it down and re-grasp.
- The arm overshoots the target — correct the motion instead of resetting the episode.

The important part is that every episode still **ends in success**: the failure and the recovery are both inside the recorded trajectory. Episodes that fail and stay failed teach the policy to give up, so those should be discarded.

A useful rule of thumb is to keep a clear majority of clean demonstrations and mix in a smaller fraction of failure-then-recovery episodes, spread over the failure modes that actually happen on the hardware.

## Next steps

Go to [`examples/MAV_handsover/README.md`](examples/MAV_handsover/README.md) for dataset handling, the finetuning script, and open-/closed-loop evaluation commands.
