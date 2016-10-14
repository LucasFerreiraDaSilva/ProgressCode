package com.teste.progresscode.model;

import com.google.gson.annotations.SerializedName;

/**
 * Created by lucas on 13/10/16.
 */

public class Meta {

    @SerializedName("limit")
    private int limit;

    @SerializedName("next")
    private int next;

    @SerializedName("offset")
    private int offset;

    @SerializedName("previous")
    private int previous;

    @SerializedName("total_count")
    private int totalCount;

    public Meta(int limit, int next, int offset, int previous, int totalCount) {
        this.limit = limit;
        this.next = next;
        this.offset = offset;
        this.previous = previous;
        this.totalCount = totalCount;
    }

    public int getLimit() {
        return limit;
    }

    public void setLimit(int limit) {
        this.limit = limit;
    }

    public int getNext() {
        return next;
    }

    public void setNext(int next) {
        this.next = next;
    }

    public int getOffset() {
        return offset;
    }

    public void setOffset(int offset) {
        this.offset = offset;
    }

    public int getPrevious() {
        return previous;
    }

    public void setPrevious(int previous) {
        this.previous = previous;
    }

    public int getTotalCount() {
        return totalCount;
    }

    public void setTotalCount(int totalCount) {
        this.totalCount = totalCount;
    }
}
