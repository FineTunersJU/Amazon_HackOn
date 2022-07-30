
from transformers import RobertaTokenizer,pipeline
import torch

model_name = "roberta-base"
tokenizer = RobertaTokenizer.from_pretrained(model_name)

model = torch.load(r'D:\Amazon HackOn\NLP_APP\ft-roberta-amazonreviews.pt',map_location=torch.device('cpu'))

def sentiment_predict(text):
    ans=pipeline("sentiment-analysis")
    return ans(text)

def predict(query, model, tokenizer, device="cpu"):
    tokens = tokenizer.encode(query)
    all_tokens = len(tokens)
    tokens = tokens[:tokenizer.model_max_length - 2]
    used_tokens = len(tokens)
    tokens = torch.tensor([tokenizer.bos_token_id] + tokens + [tokenizer.eos_token_id]).unsqueeze(0)
    mask = torch.ones_like(tokens)

    with torch.no_grad():
        logits = model(tokens.to(device), attention_mask=mask.to(device))[0]
        probs = logits.softmax(dim=-1)

    fake, real = probs.detach().cpu().flatten().numpy().tolist()
    return real

# print(type(predict("I love this product", model, tokenizer)))
# print(sentiment_predict("I hate this product")[0]['label'])