function ReviewStep({data}){


return(

<div>


<h2>
Review + Create
</h2>


<pre>

{JSON.stringify(data,null,2)}

</pre>


</div>

)


}


export default ReviewStep;