let index = new Vue({
  el: '#index',
  name: 'index',
  data: {
    posts: [],
    userComment: "",
    secretCode: ""
  },

  methods : {

    saveCode: function (){
      localStorage.setItem('secretCode', document.getElementById('secretCode').value);
        this.secretCode = localStorage.getItem("secretCode");
    },

    clearCode: function(){
      localStorage.removeItem('secretCode');
      this.secretCode = "";
    },
    like: function (post) {
      const id = post.id;
      axios.post(`/post/${id}/like`)
      .then((res) => {
        post.likes++;
      })
      .catch((err) => {
        console.log(err);
      })
    },
    comment: function (id, comment) {
      const data = {
        'comment': comment
      }
      axios.post(`/post/${id}/comment`, data)
      .then((res) => {
        window.location.replace('/');
      })
      .catch((err) => {
        console.log(err);
      })
    },
    deleteComment: function (id) {
      axios.get(`/comment/${id}/${this.secretCode}`)
      .then((res) => {
        window.location.replace('/');
      })
      .catch((err) => {
        console.log(err);
      })
    },
    deletePost: function (id) {
      axios.get(`/post/${id}/${this.secretCode}`)
      .then((res) => {
        window.location.replace('/');
      })
      .catch((err) => {
        console.log(err);
      })
    }
  },
  created: function () {
    axios.get('/post/all')
    .then((res) => {
      console.log(res);
      this.secretCode = localStorage.getItem("secretCode");
      this.posts = res.data;
       this.posts.forEach((post) => {
        post.totalComments = post.comments.length;
         console.log(post.totalComments);
        });
      return Promise.resolve();
    })
    .catch((err) => {
      console.log(err);
    });
  }
})
