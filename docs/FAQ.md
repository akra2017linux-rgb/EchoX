# FAQ - Perguntas Frequentes

## 🎵 Funcionalidade do Reprodutor

### P: Como adiciono minhas músicas?
R: Clique em "Add Folder" ou no ícone de pasta. Selecione a pasta contendo suas músicas MP3. EchoX fará uma varredura profunda, incluindo subpastas.

### P: Quais formatos de áudio são suportados?
R: Atualmente, apenas **MP3** é suportado. Suporte para WAV, FLAC e M4A está planejado para futuras versões.

### P: Como faço backup de minha biblioteca de músicas?
R: Sua biblioteca é salva em `%APPDATA%\EchoX\library.json`. Faça backup deste arquivo para preservar suas coleções.

### P: Posso criar playlists?
R: Não na versão 1.0.0, mas isto está planejado para versões futuras! Acompanhe o [Roadmap](../README.md#-roadmap).

---

## 🎨 Interface e Aparência

### P: Como mudo para tema claro?
R: Você pode editar o arquivo `config.json` e alterar `"theme": "dark"` para `"theme": "light"`. Esta feature será integrada ao menu em breve.

### P: As cores podem ser customizadas?
R: Sim! Edite o arquivo `config.json` na seção `"colors"` com seus códigos hexadecimais preferidos.

### P: A janela é redimensionável?
R: Sim, você pode redimensionar a janela. O tamanho será lembrado na próxima abertura.

---

## ⌨️ Atalhos de Teclado

### P: Qual é a lista completa de atalhos?
R: Veja a tabela de atalhos no [README.md](../README.md#-keyboard-shortcuts)

### P: Posso customizar os atalhos?
R: Não na versão atual, mas isto está sendo considerado para futuras versões.

### P: Os atalhos funcionam mesmo quando EchoX está minimizado?
R: Sim! Os atalhos globais (F5-F8) funcionam mesmo com a aplicação minimizada.

---

## 🎼 Busca e Filtros

### P: Como a busca funciona?
R: Digite na barra de busca qualquer informação: título da música, artista, álbum ou nome do arquivo. A busca é em tempo real.

### P: A busca é sensível a maiúsculas/minúsculas?
R: Não, a busca ignora maiúsculas/minúsculas (case-insensitive).

### P: Posso salvar buscas?
R: Não é possível salvar buscas como favoritas, mas você pode salvar música na biblioteca.

---

## 🖼️ Capas de Álbuns

### P: Por que algumas capas não aparecem?
R: A música deve ter tags ID3v2 com a capa embutida. Use ferramentas como [MP3Tag](https://www.mp3tag.de/) para adicionar capas.

### P: Qual é o tamanho máximo da capa?
R: EchoX aceita capas até 4MB, mas recomendamos manter abaixo de 500KB para melhor performance.

### P: Quais formatos de imagem são suportados?
R: JPEG e PNG são suportados.

---

## 🔊 Áudio e Reprodução

### P: Por que não há som?
R: 1. Verifique o volume do Windows
2. Teste o áudio em outra aplicação
3. Verifique os drivers de áudio
4. Tente um arquivo MP3 diferente
5. Reinstale Pygame: `pip install --upgrade pygame`

### P: Posso ajustar a qualidade de áudio?
R: A qualidade é determinada pelo arquivo MP3 original. EchoX reproduz sem alterações de qualidade.

### P: Existe equalizador?
R: Não na versão 1.0.0, mas está planejado para futuras versões.

### P: Como funciona o shuffle?
R: Clique no ícone de shuffle ou pressione F8 para ativar. As músicas serão reproduzidas em ordem aleatória.

---

## 📁 Gerenciamento de Pasta

### P: Posso adicionar múltiplas pastas?
R: Sim! Você pode adicionar quantas pastas desejar. Cada uma será escaneada separadamente.

### P: O que acontece se eu remover uma pasta?
R: As músicas dessa pasta serão removidas de sua biblioteca no EchoX, mas os arquivos não serão deletados.

### P: Posso editar o caminho de uma pasta?
R: Remova a pasta e adicione novamente com o novo caminho.

### P: EchoX monitora mudanças na pasta em tempo real?
R: Não por padrão. Use o botão "Refresh" para rescanear as pastas.

---

## 🐛 Problemas e Erros

### P: EchoX crashou, o que faço?
R: 1. Anote a mensagem de erro
2. Reinicie EchoX
3. Se persistir, delete `%APPDATA%\EchoX\config.json`
4. Reporte em [Issues](https://github.com/akra2017linux-rgb/EchoX/issues)

### P: Por que a música parou de repente?
R: Possíveis causas: arquivo corrompido, falta de permissão, arquivo deletado.

### P: Mensagens de erro no console
R: Procure a mensagem de erro em [Issues](https://github.com/akra2017linux-rgb/EchoX/issues) ou crie uma nova issue.

---

## 💾 Dados e Backup

### P: Onde são salvos meus dados?
R: Dados são salvos em `%APPDATA%\EchoX\`

### P: Posso exportar minha biblioteca?
R: Sim, copie o arquivo `library.json` de `%APPDATA%\EchoX\`

### P: Como transfero minha biblioteca para outro computador?
R: 1. Copie `%APPDATA%\EchoX\library.json`
2. Copie para o mesmo local no novo computador
3. Reinicie EchoX

---

## 🔒 Privacidade e Segurança

### P: EchoX coleta dados pessoais?
R: Não. EchoX funciona completamente offline. Nenhum dado é enviado para servidores.

### P: EchoX acessa internet?
R: Apenas para verificar atualizações (opcional). Sua biblioteca não é compartilhada.

### P: Dados de configuração são salvos com segurança?
R: Sim, no arquivo local `config.json`. Você controla completamente seus dados.

---

## 🔄 Atualizações

### P: Como atualizo para a versão mais recente?
R: 1. Faça backup de `%APPDATA%\EchoX\`
2. Baixe a nova versão em [Releases](https://github.com/akra2017linux-rgb/EchoX/releases)
3. Execute o novo instalador
4. Suas configurações serão preservadas

### P: Atualizações quebram minha biblioteca?
R: Raramente, mas sempre faça backup antes de atualizar.

---

## 📱 Compatibilidade

### P: EchoX funciona no Linux/Mac?
R: Não atualmente. Suporte cross-platform está no roadmap para futuras versões.

### P: EchoX funciona no Windows 7?
R: Não. Requer Windows 10 ou superior.

### P: Funciona em tablets/smartphones?
R: Não, EchoX é apenas para desktop Windows.

---

## 📞 Não Encontrou Sua Pergunta?

- Verifique as [Discussions](https://github.com/akra2017linux-rgb/EchoX/discussions)
- Procure nos [Issues](https://github.com/akra2017linux-rgb/EchoX/issues)
- Abra uma nova issue para relatar problemas
- Crie uma discussion para dúvidas gerais

**Obrigado por usar EchoX!** 🎵
