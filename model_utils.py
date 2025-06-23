
model_name_map = {
    "meta-llama/Llama-3.1-8B-Instruct": "LLaMA-3.1-8B-Instruct",
    "mistralai/Mistral-7B-Instruct-v0.3": "Mistral-7B-Instruct",
}

def get_num_blocks(model_name):
    return {
        "Llama-3.1-8B-Instruct":        32,
        "Mistral-7B-Instruct-v0.3":     32,
    }[model_name]

def get_hidden_dim(model_name):
    return {
        "Llama-3.1-8B-Instruct":        4096,
        "Mistral-7B-Instruct-v0.3":     4096,
    }[model_name]


def get_layer_names(model_name):
    num_blocks = get_num_blocks(model_name)
    return [f"model.layers.{i}" for i in range(num_blocks)]
