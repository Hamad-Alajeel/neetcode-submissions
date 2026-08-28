class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "_$_"
        else:
            return "_$_".join(item+"_^_" if item == "" else item for item in strs)

    def decode(self, s: str) -> List[str]:
        if s == "_$_":
            return []
        else:
            decoded = s.split("_$_")
            return [item.replace("_^_","") for item in decoded]