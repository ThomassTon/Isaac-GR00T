from gr00t.configs.data.embodiment_configs import register_modality_config
from gr00t.data.embodiment_tags import EmbodimentTag
from gr00t.data.types import (
    ActionConfig,
    ActionFormat,
    ActionRepresentation,
    ActionType,
    ModalityConfig,
)


mav_config = {
    "video": ModalityConfig(
        delta_indices=[0],
        modality_keys=["head", "wrist_left", "wrist_right"],
    ),
    "state": ModalityConfig(
        delta_indices=[0],
        modality_keys=[
            "eef_xyz_left",
            "eef_quat_left",
            "eef_xyz_right",
            "eef_quat_right",
            "gripper"
        ],
    ),
    "action": ModalityConfig(
        delta_indices=list(range(0, 16)),
        modality_keys=[
            "eef_xyz_left",
            "eef_quat_left",
            "eef_xyz_right",
            "eef_quat_right",
            "gripper"
        ],
        action_configs=[
            ActionConfig(
                rep=ActionRepresentation.RELATIVE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
            ActionConfig(
                rep=ActionRepresentation.ABSOLUTE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
            ActionConfig(
                rep=ActionRepresentation.RELATIVE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
            ActionConfig(
                rep=ActionRepresentation.ABSOLUTE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
            ActionConfig(
                rep=ActionRepresentation.ABSOLUTE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
        ],
        
    ),
    "language": ModalityConfig(
        delta_indices=[0],
        modality_keys=["annotation.human.task_description"],
    ),
}

# mav_config = {
#     "video": ModalityConfig(
#         delta_indices=[0],
#         modality_keys=["head", "wrist_left", "wrist_right"],
#     ),
#     "state": ModalityConfig(
#         delta_indices=[0],
#         modality_keys=[
#             "joint",
#             "gripper"
#         ],
#     ),
#     "action": ModalityConfig(
#         delta_indices=list(range(0, 16)),
#         modality_keys=[
#             "joint",
#             "gripper"
#         ],
#         action_configs=[
#             ActionConfig(
#                 rep=ActionRepresentation.RELATIVE,
#                 type=ActionType.NON_EEF,
#                 format=ActionFormat.DEFAULT,
#             ),
#             ActionConfig(
#                 rep=ActionRepresentation.ABSOLUTE,
#                 type=ActionType.NON_EEF,
#                 format=ActionFormat.DEFAULT,
#             ),
#         ],
        
#     ),
#     "language": ModalityConfig(
#         delta_indices=[0],
#         modality_keys=["annotation.human.task_description"],
#     ),
# }

register_modality_config(mav_config, embodiment_tag=EmbodimentTag.MAV)
