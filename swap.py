def swap_last_item(List):
    a=len(List)
    number=List[0]
    # Assigns the list to the variable number
    List[0]=List[a-1]
    List[a-1]=number
    return List
