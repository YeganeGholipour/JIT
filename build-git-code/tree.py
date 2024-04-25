# import struct

# class Tree:
#     # ENTRY_FORMAT = "Z*H40"
#     MODE = "100644"

#     def __init__(self, entries):
#         self.entries = entries
    
#     def type(self):
#         return "tree"
    
#     def __str__(self):
#         entries = []
#         sorted_entries = sorted(self.entries, key= lambda entry: entry.name)

#         for entry in sorted_entries:
#             content = [f"{Tree.MODE} {entry.name}", entry.oid]
#         packed_data = struct.pack(Tree.ENTRY_FORMAT, content)
#         entries.append(packed_data)

#         return "".join(entries)      


import struct

class Tree:
    ENTRY_FORMAT = "40s"  # Equivalent to "Z*H40" in Ruby
    MODE = "100644"

    def __init__(self, entries):
        self.entries = entries
    
    def type(self):
        return "tree"
    
    def __str__(self):
        entries = []
        sorted_entries = sorted(self.entries, key=lambda entry: entry.name)

        for entry in sorted_entries:
            # Convert entry.name and entry.oid to bytes
            name_bytes = entry.name.encode('utf-8')
            oid_bytes = entry.oid.encode('utf-8')
            # Append null terminator to name_bytes
            name_bytes += b'\x00'
            # Pack each entry using the format string '40s'
            packed_entry = struct.pack(Tree.ENTRY_FORMAT, name_bytes) + oid_bytes
            entries.append(packed_entry)

        return b"".join(entries).decode('utf-8')  # Decode bytes to string for output
