

async function goFetch(){

    $('#app-img-switch').html('<img src="/media/super_cat_hunt.jpg" class="rounded-circle">')

    var query = $('#input-query').val() 

    var req_data = {"query":query}

    var resp = await axios.post('/sendme', req_data)

    
    var resp_data = resp.data

    if (resp_data["STATUS"] == 'n'){


        var message = resp_data["RES"]

        var error_html = `
             
        <thead>
        <tr>
          <th>Error </th>
        </tr>
        </thead>
        <tbody>
         <tr>
           <td>${message}</td>
         </tr>
        </tbody>        
        
        `


        $('#app-result-render').html(error_html)


    } else {

        var records = resp_data["RES"]


        var result_html  = `
        <thead>
          <tr>
            <th>Index </th>
            <th> Word</th>
          </tr>
        </thead>
        <tbody id="app-result-render-body">
        </tbody>
        `


        $('#app-result-render').html(result_html)

        for (let i=0;i<records.length;i++){

            var res_idx = records[i]["IDX"]

            var res_word = records[i]["WORD"]

            var body_html = `
            <tr>
                <td> ${res_idx} </td>
                <td> ${res_word} </td>
            </tr>
            
            `
            $('#app-result-render-body').append(body_html)

        }

        
    }

    $('#app-img-switch').html('<img src="/media/super_cat.jpg" class="rounded-circle">')
}

