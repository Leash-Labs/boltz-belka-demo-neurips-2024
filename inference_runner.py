from datetime import datetime
import os
import sky

cluster_name = os.environ.get("CLUSTER_NAME", None)

input_dir = "./boltz-inputs"
output_dir = "./boltz-outputs"
recycling_steps = 3
devices = 4

run_cmd = (
    'pip install poetry && '
    'poetry install --no-interaction && '
    f'poetry run boltz predict "{input_dir}" --out_dir "{output_dir}" --recycling_steps {recycling_steps} --devices {devices} --use_msa_server'
)

per_trial_resources = sky.Resources(
    accelerators={"A10G": devices},
    use_spot=True,
)

formatted_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
task = sky.Task(
    name=f"skypilot-boltz-inference-{formatted_time}",
    run=run_cmd,
    workdir='./'
).set_resources(
    per_trial_resources
)

sky.launch(
    task,
    cluster_name=cluster_name,
    stream_logs=True,
    detach_run=False,
)