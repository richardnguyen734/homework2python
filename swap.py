def swap_last_item(List):
    a=len(List)
    number=List[0]
    List[0]=List[a-1]
    List[a-1]=number
    return List
