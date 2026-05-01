import re

class DataValidator:
    @staticmethod
    def is_valid_cnpj_headquarters(cnpj: str) -> bool:
        """
        Checks if the CNPJ corresponds to a headquarters (mil contra '0001').
        The digits from position 9 to 12 must be '0001'.
        """
        # Remove non-numeric characters
        clean_cnpj = re.sub(r'\D', '', str(cnpj))
        
        # Ensure it has 14 digits
        if len(clean_cnpj) != 14:
            return False
            
        # Positions 9 to 12 (0-indexed: 8, 9, 10, 11)
        mil_contra = clean_cnpj[8:12]
        return mil_contra == "0001"

    @staticmethod
    def format_cnpj(cnpj: str) -> str:
        """
        Applies the mask 00.000.000/0000-00 to a CNPJ string, preserving leading zeros.
        """
        clean_cnpj = re.sub(r'\D', '', str(cnpj))
        
        # Ensure it has 14 digits by padding with leading zeros if necessary
        if clean_cnpj.isdigit():
            clean_cnpj = clean_cnpj.zfill(14)
            
        if len(clean_cnpj) != 14:
            return clean_cnpj
            
        return f"{clean_cnpj[:2]}.{clean_cnpj[2:5]}.{clean_cnpj[5:8]}/{clean_cnpj[8:12]}-{clean_cnpj[12:]}"

    @staticmethod
    def format_competencia(competencia: str) -> str:
        """
        Prefixes '01/' to the competency string (expected mm/aaaa).
        """
        if not competencia or str(competencia) == 'nan':
            return ""
        return f"01/{competencia}"
