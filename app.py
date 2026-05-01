import streamlit as st
from processor import FileProcessor
import time
import zipfile
import io

class InterfaceManager:
    def __init__(self):
        self.processor = FileProcessor()

    def run(self):
        st.set_page_config(page_title="Processamento eConsignado", layout="wide")
        st.title("🚀 Sistema de Processamento eConsignado")
        st.markdown("---")

        # Mudança para aceitar múltiplos arquivos
        uploaded_files = st.file_uploader(
            "Selecione uma ou mais planilhas de origem", 
            type=["xlsx"], 
            accept_multiple_files=True
        )

        if uploaded_files:
            if st.button(f"Processar {len(uploaded_files)} arquivo(s)"):
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                # Buffer para o arquivo ZIP final
                zip_buffer = io.BytesIO()
                
                with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
                    all_logs = []
                    
                    for i, uploaded_file in enumerate(uploaded_files):
                        file_name = uploaded_file.name
                        status_text.text(f"Processando: {file_name}...")
                        
                        # Processar o arquivo individualmente
                        result, message = self.processor.process(uploaded_file)
                        
                        if result:
                            # Adicionar ao ZIP com o nome dinâmico gerado pelo processador
                            zip_file.writestr(self.processor.output_filename, result.getvalue())
                            all_logs.append(f"✅ {file_name} -> {self.processor.output_filename}")
                        else:
                            all_logs.append(f"❌ {file_name}: {message}")
                        
                        # Adicionar logs internos do processador
                        if self.processor.logs:
                            all_logs.extend([f"  - {log}" for log in self.processor.logs])
                        
                        # Atualizar progresso
                        progress_percent = int(((i + 1) / len(uploaded_files)) * 100)
                        progress_bar.progress(progress_percent)

                    status_text.text("Todos os arquivos processados!")
                    
                zip_buffer.seek(0)
                
                st.success(f"Processamento concluído: {len(uploaded_files)} arquivo(s).")
                
                # Botão de download para o arquivo ZIP
                st.download_button(
                    label="📥 Baixar Todas as Planilhas (ZIP)",
                    data=zip_buffer,
                    file_name="Planilhas_eConsignado_Processadas.zip",
                    mime="application/zip"
                )

                # Exibição de Logs
                with st.expander("Ver Resumo do Processamento"):
                    for log in all_logs:
                        st.write(log)

if __name__ == "__main__":
    app = InterfaceManager()
    app.run()
