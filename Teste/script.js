const postForm = document.getElementById('post-form');
const postList = document.getElementById('post-list');
const filterCategory = document.getElementById('filter-category');

let posts = [];

// Carrega posts do localStorage
if (localStorage.getItem('posts')) {
  posts = JSON.parse(localStorage.getItem('posts'));
  renderPosts();
}

// Função para atualizar o carrossel de imagens
function updateCarousel(postId, direction) {
  const postElement = document.querySelector(`li[data-post-id="${postId}"]`);
  if (!postElement) return;

  const images = postElement.querySelectorAll('.post-image');
  const currentImageIndex = Array.from(images).findIndex(image => image.classList.contains('active'));

  let nextImageIndex;
  if (direction === 'prev') {
    nextImageIndex = (currentImageIndex - 1 + images.length) % images.length;
  } else if (direction === 'next') {
    nextImageIndex = (currentImageIndex + 1) % images.length;
  } else {
    return;
  }

  images.forEach(image => image.classList.remove('active'));
  images[nextImageIndex].classList.add('active');
}

// Função para renderizar os posts
function renderPosts() {
  postList.innerHTML = ''; // Limpa a lista de posts

  const filteredPosts = filterCategory.value ? posts.filter(post => post.category === filterCategory.value) : posts;

  filteredPosts.forEach(post => {
    const listItem = document.createElement('li');
    listItem.dataset.postId = post.id; // Adiciona o postId ao elemento li

    // Cria a div do post
    const postDiv = document.createElement('div');
    postDiv.innerHTML = `
      <h3>${post.text}</h3>
      <p>Categoria: ${post.category}</p>
      <p>Data: ${post.date}</p>
      <div class="post-image-carousel">
        ${post.images.map((image, index) => 
          `<img class="post-image ${index === 0 ? 'active' : ''}" src="${image}" alt="Imagem do post">`
        ).join('')}
      </div>
      <div class="carousel-buttons">
        <button class="prev-button" data-post-id="${post.id}">❮</button>
        <button class="next-button" data-post-id="${post.id}">❯</button>
      </div>
      <div class="edit-delete-buttons">
        <button class="edit-button" data-post-id="${post.id}">Editar</button>
        <button class="delete-button" data-post-id="${post.id}">Excluir</button>
      </div>
    `;

    // Adiciona a div do post à lista de posts
    listItem.appendChild(postDiv);
    postList.appendChild(listItem);
  });

  // Adiciona eventos para os botões de navegação do carrossel (apenas uma vez)
  if (!postList.querySelector('.prev-button').hasEventListener('click', handlePrevClick)) {
    const prevButtons = postList.querySelectorAll('.prev-button');
    const nextButtons = postList.querySelectorAll('.next-button');

    const handlePrevClick = () => {
      updateCarousel(this.dataset.postId, 'prev');
    };

    const handleNextClick = () => {
      updateCarousel(this.dataset.postId, 'next');
    };

    prevButtons.forEach(button => {
      button.addEventListener('click', handlePrevClick);
    });

    nextButtons.forEach(button => {
      button.addEventListener('click', handleNextClick);
    });
  }

  // Adiciona eventos para os botões de edição e exclusão
  const editButtons = postList.querySelectorAll('.edit-button');
  const deleteButtons = postList.querySelectorAll('.delete-button');

  editButtons.forEach(button => {
    button.addEventListener('click', () => editPost(button.dataset.postId));
  });

  deleteButtons.forEach(button => {
    button.addEventListener('click', () => deletePost(button.dataset.postId));
  });
}

// Função para adicionar um novo post
postForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const text = document.getElementById('text').value;
  const category = document.getElementById('category').value;
  const image1 = document.getElementById('image1').value;
  const image2 = document.getElementById('image2').value;
  const image3 = document.getElementById('image3').value;

  const newPost = {
    id: Date.now(),
    text,
    category,
    images: [image1, image2, image3].filter(image => image),
    date: new Date().toLocaleDateString(),
  };

  posts.push(newPost);
  localStorage.setItem('posts', JSON.stringify(posts));

  renderPosts();
  postForm.reset();
});

// Função para editar um post
function editPost(postId) {
  const post = posts.find(post => post.id === postId);

  // Exibe um formulário para editar o post
  // ...

  // Atualiza o post no array e no localStorage
  // ...

  // Renderiza os posts atualizados
  renderPosts();
}

// Função para excluir um post
function deletePost(postId) {
  if (confirm('Tem certeza que deseja excluir este post?')) {
    posts = posts.filter(post => post.id !== postId);
    localStorage.setItem('posts', JSON.stringify(posts));
    renderPosts();
  }
}

// Evento para filtrar os posts
filterCategory.addEventListener('change', renderPosts);

// Renderiza os posts ao carregar a página
renderPosts();