# *         모든 노드들
# div, p    div와 p노드들
# div p     div안에 있는 p노드들
# div > p   div 바로 안에 있는 p노드들
# div ~ p   p옆(앞)에 있는 div 노드들
# div + p   div옆(뒤)에 있는 p노드들


document.querySelectorAll("td.sale + td") 
document.querySelectorAll("td.sale + td + td") # 윗줄의 다음 값
