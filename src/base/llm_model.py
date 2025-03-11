import torch
from transformers import BitsAndBytesConfig
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain.llms.huggingface_pipeline import HuggingFacePipeline
from langchain_community.llms import CTransformers

nf4_config = BitsAndBytesConfig(
    load_in_4bits = True,
    bnb_4bits_quant_type = "nf4",
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=torch.bfloat16
)

def get_hf_llm(model_name: str = "Mistral-7B-Instruct-v0.1 GGUF", max_new_tokens =1024, **kwargs):
    
    # model = AutoModelForCausalLM.from_pretrained(
    #     model_name,
    #     quantization_config=nf4_config,
    #     low_cpu_mem_usage = True
    # )
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="cpu"  # Chạy mô hình trên CPU
    )

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    model_pipeline = pipeline(
        "text-generation",
        model= model,
        tokenizer=tokenizer,
        max_new_tokens = max_new_tokens,
        pad_token_id = tokenizer.eos_token_id,
        device_maps = "auto"
    )


    llm = HuggingFacePipeline(
        pipeline=model_pipeline,
        model_kwargs = kwargs
    )

    return llm


def get_llama_llm(model_file, max_new_tokens=1024, temperature=0.9, gpu_layers=0):
    llm = CTransformers(
        model=model_file,  # Đường dẫn đến file .gguf
        model_type="llama",
        config={
            "max_new_tokens": max_new_tokens,
            "temperature": temperature,
            "gpu_layers": gpu_layers
        }
    )
    return llm