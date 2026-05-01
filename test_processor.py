from processor import FileProcessor
import os

def test_processing():
    input_file = "Planilha origem.xlsx"
    if not os.path.exists(input_file):
        print(f"Erro: Arquivo {input_file} não encontrado.")
        return

    processor = FileProcessor()
    result, message = processor.process(input_file)
    
    print(f"Status: {message}")
    if result:
        output_name = f"TESTE_{processor.output_filename}"
        with open(output_name, "wb") as f:
            f.write(result.getbuffer())
        print(f"Arquivo gerado: {output_name}")
        
        # Check logs
        print("\nLogs de Processamento:")
        for log in processor.logs:
            print(log)

if __name__ == "__main__":
    test_processing()
