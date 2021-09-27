var convert = require('sbgnml-to-cytoscape');

const getXml = async (fname) => {
  const response = await fetch(fname)
  if (response.status === 200) {
    return await response.text();
  } else {
    throw new Error('Unable to get your location')
  }
}

var toJson = function (obj) {
  return JSON.stringify(obj, null, 4);
};

var xmlText = getXml('activated_stat1alpha_induction_of_the_irf1_gene.xml').then((data) => {
    console.log(data);
    var cyGraph = convert(data);
    console.log(toJson(cyGraph));

    document.getElementById("app").innerHTML = toJson(cyGraph);
  });