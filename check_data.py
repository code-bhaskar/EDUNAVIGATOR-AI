from backend.database import documents_collection, chunks_collection
import json

def audit():
    doc_count = documents_collection.count_documents({})
    chunk_count = chunks_collection.count_documents({})
    
    print(f"\n--- DATABASE AUDIT REPORT ---")
    print(f"Total Documents: {doc_count}")
    print(f"Total Chunks:    {chunk_count}")
    
    if chunk_count > 0:
        sample = chunks_collection.find_one()
        print(f"\n[SAMPLE CHUNK]")
        print(f"ID:          {sample['_id']}")
        print(f"Document ID: {sample.get('document_id')}")
        print(f"Text Snippet: {sample['text'][:150]}...")
        print(f"Embedding Dimensions: {len(sample['embedding'])}")
        print(f"Vector Sample (first 3): {sample['embedding'][:3]}")
        
        # Check if embedding is all zeros (common error)
        if all(v == 0 for v in sample['embedding']):
            print("\nWARNING: All zero embedding detected!")
        else:
            print("\nSUCCESS: Embeddings are non-zero and valid.")
    else:
        print("\nWARNING: No chunks found in database.")

if __name__ == "__main__":
    audit()
