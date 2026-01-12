package katas;

import java.util.List;
import java.util.Map;
import java.util.HashMap;

public class PaginationHelper<I> {

    private List<I> collection;
    private int itemsPerPage;
    private Map<Integer, List<I>> pages = new HashMap<>();

    public PaginationHelper(List<I> collection, int itemsPerPage) {
        this.collection = collection;
        this.itemsPerPage = itemsPerPage;
        buildPages();
    }

    private void buildPages() {
        pages.clear();
        int pageCount = (collection.size() + itemsPerPage - 1) / itemsPerPage; // redondea hacia arriba

        for (int page = 0; page < pageCount; page++) {
            int start = page * itemsPerPage;
            int end = Math.min(start + itemsPerPage, collection.size());
            pages.put(page, collection.subList(start, end));
        }
    }

    public int itemCount() {
        return collection.size();
    }

    public int pageCount() {
        return pages.size();
    }

    public int pageItemCount(int pageIndex) {
        if (!pages.containsKey(pageIndex)) return -1; 
        return pages.get(pageIndex).size();
    }

    public int pageIndex(int itemIndex) {
        if (itemIndex < 0 || itemIndex >= collection.size()) return -1;
        return itemIndex / itemsPerPage; // división entera, cero-based
    }
}
