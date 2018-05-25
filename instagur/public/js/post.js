let post = new Vue({
  el: '#post',
  name: 'post',
  data: {
    placeholder: "",
    post: {
      image: "",
      content: "",
    }
  },
  methods: {
    makePost: function () {
      let data = new FormData();
      data.append('file', this.post.image);
      data.append('content', this.post.content);
      axios.post('/post', data)
      .then((res) => {
        window.location.replace('/');
      })
      .catch((err) => {
        console.log(err);
      })
    },
    addUpload: function () {
      document.getElementById('upload').click();
    },
    processUpload: function (event) {
      let reader = new FileReader();
      reader.onload = (e) => {
        this.placeholder = e.target.result;
      }
      reader.readAsDataURL(event.target.files[0]);
      console.log(event.target.files[0]);
      this.post.image = event.target.files[0];
    }
  }
})
