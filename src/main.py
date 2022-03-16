from sentence_transformers import SentenceTransformer, util
import torch
import json

class SemanticSearch:


    def ___init__():
        pass

    def train_model(self):
        embedder = SentenceTransformer('all-MiniLM-L6-v2')
        corpus = ['A man is eating food.',
                'A man is eating a piece of bread.',
                'The girl is carrying a baby.',
                'A man is riding a horse.',
                'A woman is playing violin.',
                'Two men pushed carts through the woods.',
                'A man is riding a white horse on an enclosed ground.',
                'A monkey is playing drums.',
                'A cheetah is running behind its prey.'
                ]
        corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)
        return corpus,corpus_embeddings,embedder


    def predict_sem(self,queries):#queries = ['A man is eating pasta.', 'Someone in a gorilla costume is playing a set of drums.']
        corpus,corpus_embeddings,embedder=self.train_model()
        top_k = min(3, len(corpus))
        all=[]
        for query in queries:
            query_embedding = embedder.encode(query, convert_to_tensor=True)
            # We use cosine-similarity and torch.topk to find the highest 5 scores
            cos_scores = util.cos_sim(query_embedding, corpus_embeddings)[0]
            top_results = torch.topk(cos_scores, k=top_k)
            print("Query:", query)
            print("\nTop 3 most similar sentences in corpus:")
            matched=[]
            scores=[]
            for score, idx in zip(top_results[0], top_results[1]):
                results=corpus[idx]
                score="{:.4f}".format(score)
                matched.append(results)
                scores.append(score)
            val={"matched": matched},{"scores": scores}
            all.append(val)
        return all
