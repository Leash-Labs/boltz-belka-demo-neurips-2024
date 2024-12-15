from datetime import datetime  # Import datetime to handle date and time operations
import os  # Import os to interact with the operating system
import sky  # Import SkyPilot for managing cloud resources and tasks

# Retrieve the cluster name from environment variables, if set
cluster_name = os.environ.get("CLUSTER_NAME", None)

# Define the directory where Boltz input files are stored
input_dir = "./boltz-inputs"

# Define the directory where Boltz output files will be saved
output_dir = "./boltz-outputs"

# Set the number of recycling steps for Boltz predictions
recycling_steps = 3

# Number of GPU devices to use
devices = 4

# Define the command to run Boltz predictions
run_cmd = (
    'pip install poetry && '  # Install Poetry, the dependency manager
    'poetry install --no-interaction && '  # Install project dependencies without interaction
    f'poetry run boltz predict "{input_dir}" --out_dir "{output_dir}" '
    f'--recycling_steps {recycling_steps} --devices {devices} --use_msa_server'  # Run Boltz with specified parameters
)

# Define the resources required for each SkyPilot task
per_trial_resources = sky.Resources(
    accelerators={"A10G": devices},  # Specify the type and number of GPU accelerators
    use_spot=True,  # Use spot instances to reduce costs
)

# Format the current time to create a unique task name
formatted_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Create a new SkyPilot task with the specified configurations
task = sky.Task(
    name=f"skypilot-boltz-inference-{formatted_time}",  # Name the task with a timestamp
    run=run_cmd,  # Command to execute the prediction
    workdir='./'  # Set the working directory for the task
).set_resources(
    per_trial_resources  # Assign the defined resources to the task
)

# Launch the SkyPilot task with the specified cluster and configurations
sky.launch(
    task,  # The task to be launched
    cluster_name=cluster_name,  # Specify the cluster name if provided
    stream_logs=True,  # Stream the logs to the console for real-time monitoring
    detach_run=False,  # Wait for the task to complete before continuing
)