from SyT import SymbolTable

if __name__ == "__main__":
    st = SymbolTable()
    st.add("m")
    st.add("l")
    assert (st.add("a")==2)
    print(st)