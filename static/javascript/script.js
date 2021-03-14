//getting modal section

function modal(){


    let openModal = document.querySelector('button');


    openModal.onclick = function(){
    
    
        let modal = openModal.getAttribute('data-modal');
    
        console.log('clicked')
    
        document.getElementById(modal).style.display = 'flex';
    
    
    };
    
    
    let closeModal = document.querySelector('.close-modal');
    
    closeModal.onclick = function(){
    
    
        let modal = (closeModal.closest(".modal").style.display='none');
    
    
    };


}



function goals(){
    
    const progress = document.querySelector('.progress button');

    progress.onclick = function(){


        if (progress.innerHTML === "Close"){

            document.getElementById('p').style.display="none";
            progress.innerHTML = "View Progress";
    
        }
    
        else{
    
            document.getElementById('p').style.display="block";
            progress.innerHTML = "Close";
    
        }
    
    

    }


    





}

goals();
modal();