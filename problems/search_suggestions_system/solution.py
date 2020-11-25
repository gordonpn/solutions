class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        results: List[List[str]] = []
        products.sort()
        
        searchChar = ""
        for char in searchWord:
            searchChar += char
            iterative_results: List[str] = []
            for product in products:
                if product.startswith(searchChar):
                    iterative_results.append(product)
                if len(iterative_results) == 3:
                    break
            results.append(iterative_results)
            
        return results
