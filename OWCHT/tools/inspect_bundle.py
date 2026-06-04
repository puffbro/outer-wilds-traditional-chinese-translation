import UnityPy

bundle_path = r'C:\Users\Chloe\AppData\Roaming\OuterWildsModManager\OWML\Mods\PuFF.OWCHT\Assets\owcht'
env = UnityPy.load(bundle_path)

for path, obj in env.container.items():
    if obj.type.name != 'Font':
        continue
    data = obj.read_typetree()
    name = data.get('m_Name')
    char_rects = data.get('m_CharacterRects') or []
    if not char_rects:
        continue

    baked_indices = {cr['index'] for cr in char_rects}
    print(f"=== {name} ({len(baked_indices)} chars baked) ===")

    check = {'螢': ord('螢'), '採': ord('採')}
    for char, code in check.items():
        found = code in baked_indices
        print(f"  U+{code:04X} '{char}' -> {'OK' if found else 'MISSING'}")

    # 也列出所有 baked 字符供參考
    chars = ''.join(chr(i) for i in sorted(baked_indices) if i > 127)
    print(f"  Baked CJK sample: {chars[:80]}...")
