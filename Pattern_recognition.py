# Pattern Recognitiona Search for TLR4 protein using different time complexity
# For Example:
# items = ['frag1', 'frag2', 'frag3']

# def is_present(item: str) -> bool:
#    return item in items
    
# print(is_present('frag1'))
# print(is_present('frag4'))

# items_set = {'frag1', 'frag2', 'frag3'}

# def is_present(item: str) -> bool:
#    return item in items_set
    
# print(is_present('frag1'))
# print(is_present('frag4'))

sequence = "MFPVLSLLLPLLLAGASQGPEAPTQDGFLSFCRIQNFFWENSIRHMLQSCYNFEAFSLPFTLKNHCIIYVDKWWNIFFKFLPFSLNLSFIDFTLVFLLFLFIIFMISILILTRFKFRRHFWLQLKQISVFLSSILLLVGLVAIDRNFISLHFRKILHILSQDIQLVSNCSNLSSTLQAALNLTALGNAIEEEKLISQKASNNLSTLAFKENTLQQLREQMQSLDNLSTLKDVQSTCSNSSDLSSSTLQQLRDELFTRLSDMQGLSLAGQQFQEALNVLQLQKTVLQRVLEKISLMGLQEAQKESPFTYMTLLSAFRVQNSQWKFHDSLFSFLGLLLNTPDSFNVKAAEIHSLFSSVANPMFGPLKTFSSSTLLFSLVLDPSLSLENSFGLLKNLSLSSPNDILGLVKFNRVLDLSLEKISQSGLL"

def generate_fragments_as_items(sequence, num_fragments):
    fragment_size = len(sequence) // num_fragments
    fragments = [sequence[i:i+fragment_size] for i in range(0, len(sequence), fragment_size)]
    items = [f"fragment{i+1}" for i in range(num_fragments)]
    fragments_with_items = dict(zip(items, fragments))
    return fragments_with_items

fragments_as_items = generate_fragments_as_items(sequence, 50)

for item, fragment in fragments_as_items.items():
    print(f"{item}: {fragment}")

def is_present(item: str, fragments: dict) -> bool:
    return item in fragments.values()

print(is_present('NLSLSSPN', fragments_as_items))

