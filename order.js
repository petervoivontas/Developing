let orderCount = 0;

const takeOrder = (topping, crustType) => {
  orderCount ++;
  console.log(`Order: ${crustType} pizza topped with ${topping}`);
}

const getSubTotal = (itemCount) => {
  return itemCount * 7.5;
}

const getTax = (orderCount) => {
  return getSubTotal(orderCount) * 0.06;
}

const getTotal = () => {
  return getSubTotal(orderCount) + getTax(orderCount);
}

takeOrder('bacon', 'thin crust');
takeOrder('bacon', 'thin crust');
takeOrder('bacon', 'thin crust');
console.log(getSubTotal(orderCount));
console.log(getTotal());