def find_segments(data):
    all_segments = []
    seg = data[0]

    for l in data[1:]:
        if l == seg[-1]:
           seg = seg + l

        else:
            all_segments.append((len(seg), seg[0]))
            seg = l
    all_segments.append((len(seg), seg[0]))
    return all_segments
           
           
           
    




if __name__ == "__main__":
    print(find_segments("aaabbccdddd"))
    # [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]

    print(find_segments("aaaaaaaaaaaaaaaaaaaa"))
    # [(20, 'a')]

    print(find_segments("abcabc"))
    # [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]

    print(find_segments("kissa"))
    # [(1, 'k'), (1, 'i'), (2, 's'), (1, 'a')]