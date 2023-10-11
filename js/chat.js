document.addEventListener("DOMContentLoaded", function() {
    const chatIcon = document.getElementById("chat-icon");
    const chatContainer = document.getElementById("chat-container");
    const closeButton = document.getElementById("close-button");
  
    function showMessage(message, sender) {
      const messageContainer = document.createElement("div");
      messageContainer.classList.add("message", sender);
      messageContainer.innerHTML = `<p>${message}</p>`;
      const chatBody = document.getElementById("chat-body");
      chatBody.appendChild(messageContainer);
      chatBody.scrollTop = chatBody.scrollHeight;
    }
  
    function processQuestion(question) {
      let answer;
  
      switch (question) {
        case "Me diga as aulas que mais atendemos alunos.":
          answer = "--Aulas com mais atendimentos-- HIIT 667 <br/> Cycling 376 <br/> Strength 233 <br/> Yoga 135 <br/> Aqua 76 <br/> Others  13";
          break;
        case "Me diga os dias da semana que mais faltam alunos.":
          answer = "Wednesday - Quarta-feira <br/>  Tuesday - Terça-feira";
          break;
        case "Me diga qual horário e dia da semana há um fluxo maior de alunos.":
          answer = "No dia da semana 'Friday - <br/>Sexta-feira' no horário 'AM - antes de meio-dia' foi quando mais pessoas foram atendidas, com 295 atendimentos.";
          break;
        case "Quero fazer outra pergunta..":
          answer = "Estamos implementando a entrada de texto";
          break;
        default:
          answer = "Desculpe, não entendi sua pergunta. Por favor, selecione uma das opções disponíveis.";
          break;
      }
  
      showMessage(question, "sent");
      setTimeout(function() {
        showMessage(answer, "received");
      }, 500);
    }
  
    function createQuestionButtons() {
      const questionButtons = document.querySelectorAll(".question-buttons-container");
    
      questionButtons.forEach(function(button) {
        button.addEventListener("click", function() {
          const question = button.textContent;
          processQuestion(question);
        });
      });
    }
  
    function openChatbot() {
      chatContainer.style.display = "block";
      createQuestionButtons();
    }
  
    function closeChatbot() {
      chatContainer.style.display = "none";
    }
  
    chatIcon.addEventListener("click", openChatbot);
    closeButton.addEventListener("click", closeChatbot);
  });