<nav class="sticky-top nav-edit">
      <div class= "row">
          <div class="col-sm-1 col-md-1 col-lg-1"></div>
        <div class = 'col-sm-1 col-md-1 col-lg-1'>

        </div>
          <div class="col-sm-1 col-md-1 col-lg-1"></div>
        <div class = 'col-sm-1 col-md-1 col-lg-1'>
          <a href = "{% url 'adverts:advert-list' %}" class="a-nav">Оголошення</a>
        </div>
        <div class = 'col-sm-1 col-md-1 col-lg-1'>
          <a href = "{% url 'walking:walk-list' %}" class="a-nav">Прогулянки</a>
        </div>
        <div class="col-sm-1 col-md-1 col-lg-1">
            <a href = "{% url 'polls:question-list' %}" class="a-nav">Опитування</a>
        </div>
          <div class="col-sm-1 col-md-1 col-lg-1">
            <a href = "{% url 'ins:ins-list' %}" class="a-nav">Заклади</a>
        </div>
          <div class="col-sm-1 col-md-1 col-lg-1">
            <a href = "{% url 'events:calendar' %}" class="a-nav">Події</a>
        </div>
          <div class="col-sm-1 col-md-1 col-lg-1">
              <a href = "{% url 'news:new-list' %}" class="a-nav">Новини</a>
          </div>
          <div class="col-sm-1 col-md-1 col-lg-1">
              <div class="user-search-div">
                  <a href = "#"><img src="{% static 'images/main/search-icon.png' %}" class = "search-icon-img"></a>
                  {% if request.user.is_authenticated %}
                    <a href = "{% url 'auth:user-profile' request.user.pk %}"><img src="{% static 'images/main/user-icon.png' %}" class = "user-icon-img"></a>
                  {% else %}
                    <a href = "{% url 'auth:login' %}"><img src="{% static 'images/main/user-icon.png' %}" class = "user-icon-img"></a>
                  {% endif %}
            </div>
          </div>
          <div class="col-sm-1 col-md-1 col-lg-1"></div>
        </div>
    </nav>
</header>