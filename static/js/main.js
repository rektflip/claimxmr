window.onload = function () {
    new Vue({
    el: '#app',
    data: {
      subadr: "",
      bolenz: 0,
      hideclaim: "display:none;",
      hidecreate: "display:none;",
      hideok: "display:none;",
      hidefund: "display:none;",
      hidenobolenz: "display:none;",
      txid: "",
      qrcode: ""
    },
    mounted(){
        const queryString = window.location.search;
        const urlParams = new URLSearchParams(queryString);
        if(urlParams.get("subadr") != null){
            fetch("/claim/" + urlParams.get("subadr"))
            .then(response => response.json())
            .then((data) => {
                this.bolenz = data;
                if(this.bolenz == 0){
                    this.hidenobolenz = "display:unset;";
                }else{
                    this.hideclaim = "display:unset;"
                }
            })

            //console.log("claim");
        }else{
            console.log("create");
            this.hideclaim = "display:none;"
            this.hidecreate = "display:unset;"
        }

    },
    methods:{
        claim(){
            const queryString = window.location.search;
            const urlParams = new URLSearchParams(queryString);
            if(urlParams.get("subadr") != null){
                var inputfield = document.getElementById("address");
                if(inputfield.value){
                    this.hideclaim = "display:none;"
                    this.hidecreate = "display:none;"
                    this.hideok = "display:unset;"
                    // console.log(inputfield.value);
                    fetch("/claim/" + urlParams.get("subadr") + "/" + inputfield.value)
                    .then(response => response.text())
                    .then((data) => {
                        this.txid = data;
                    })

                }

            }

        },
        create(){
            this.hidefund = "display:unset;";
            this.hidecreate = "display:none;"
            fetch("/claim/")
            .then(response => response.text())
            .then((data) => {
                this.subadr = data;
                this.qrcode = "/img/" + this.subadr + ".png";

            })

        }

    }



  });

}
