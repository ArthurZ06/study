function zeroAEsquerda(num) {
    return num >= 10 ? num : `0${num}`;
  }
  
  function formataData(data) {
    const dia = zeroAEsquerda(data.getDate());
    const mes = zeroAEsquerda(data.getMonth() + 1); // Adiciona 1 ao mês
    const ano = zeroAEsquerda(data.getFullYear());
    const hora = zeroAEsquerda(data.getHours());
    const min = zeroAEsquerda(data.getMinutes()); // Corrigido para getMinutes()
    const seg = zeroAEsquerda(data.getSeconds());
  
    return `${dia}/${mes}/${ano} ${hora}:${min}:${seg}`; // Adiciona o formato do dia, mês e ano
  }
  
  function atualizaRelogio() {
    const data = new Date();
    const dataBrasil = formataData(data);
  
    document.getElementById("clock").textContent = dataBrasil;
  }
  
  // Chama a função atualizaRelogio a cada segundo para atualizar o relógio em tempo real
  setInterval(atualizaRelogio, 1000);
  