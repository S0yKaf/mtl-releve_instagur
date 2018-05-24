var post = new Vue({
  el: '#post',
  name: 'post',
  data: {
    post: {
      image: "",
      content: "",
    }
  },
  methods: {
    makePost: function() {
      axios.post('/upload', this.post)
      .then((res) => {
        window.location.replace('/');
      })
      .catch((err) => {
        console.log(err);
      })
    }
  }
})
