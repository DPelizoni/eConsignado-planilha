@echo off
set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

echo ====================================================
echo DIAGNOSTICO DE INICIALIZACAO
echo ====================================================
echo Pasta do Projeto: %CD%
echo.

:: Verifica se a venv existe
if not exist "venv\Scripts\activate.bat" (
    echo [ERRO] Pasta 'venv\Scripts\activate.bat' nao encontrada!
    echo Certifique-se de que voce criou o ambiente virtual nesta pasta.
    pause
    exit /b
)

echo [OK] Ambiente virtual encontrado.
echo Tentando iniciar o Streamlit...
echo.

:: Executa o comando e NÃO fecha a janela se houver erro
call venv\Scripts\activate.bat
python -m streamlit run app.py --server.port 8501 --server.headless false

if %errorlevel% neq 0 (
    echo.
    echo ====================================================
    echo [ERRO] O Streamlit falhou ao iniciar. 
    echo Verifique as mensagens acima para entender o motivo.
    echo ====================================================
)

:: O 'pause' aqui garante que a janela nao feche sozinha se falhar
pause
