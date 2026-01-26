set -x -e

export NUM_GPUS=1

# torchrun --nproc_per_node=$NUM_GPUS --master_port=29500 \
CUDA_VISIBLE_DEVICES=0 python \
    gr00t/experiment/launch_finetune.py \
    --base_model_path nvidia/GR00T-N1.6-3B \
    --dataset_path  data/MAV_Sort \
    --modality_config_path examples/MAV_SORT/mav_config.py \
    --embodiment_tag MAV \
    --num_gpus $NUM_GPUS \
    --output_dir log/mav_finetune_sort \
    --save_steps 5000 \
    --save_total_limit 20 \
    --max_steps 50000 \
    --warmup_ratio 0.05 \
    --weight_decay 1e-5 \
    --learning_rate 1e-4 \
    --use_wandb \
    --global_batch_size 32 \
    --color_jitter_params brightness 0.3 contrast 0.4 saturation 0.5 hue 0.08 \
    --dataloader_num_workers 4
